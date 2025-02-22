import sys
import threading
import markdown

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QPixmap
from tzlocal import get_localzone

import util.web as web
from ui_form import Ui_MainWindow
from util.misc import append_timestamp, read_config, write_config, parse_target_url, parse_refresh_time


class Communicator(QObject):
    # Communicator object allowing for external data to be ported into GUI
    external_log = Signal(str)
    counter_update = Signal(int)
    timeout_error = Signal(bool)

    def __init__(self):
        super().__init__()
        self.running = False
        self.driver = None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1150, 563)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.comm = Communicator()
        self.comm.external_log.connect(self.external_log)
        self.comm.counter_update.connect(self.update_counter)
        self.comm.timeout_error.connect(self.activate_timeout_error)

        # Connect fields to functions
        self.ui.product_display_list.itemClicked.connect(lambda: self.update_url_button_display('remove'))
        self.ui.url_entry_line.textChanged.connect(lambda: self.update_url_button_display('add'))
        self.ui.add_url_button.clicked.connect(self.add_product)
        self.ui.remove_url_button.clicked.connect(self.delete_selected_product)
        self.ui.product_display_list.itemDoubleClicked.connect(self.set_selected_product)
        self.ui.chrome_data_path_button.clicked.connect(self.update_data_path)
        self.ui.timezone_field.currentIndexChanged.connect(self.change_timezone)
        self.ui.chrome_profile_field.currentIndexChanged.connect(self.update_chrome_profile)
        self.ui.max_quantity_field.currentIndexChanged.connect(self.update_max_quantity)
        self.ui.refresh_time_field.currentIndexChanged.connect(self.update_refresh_time)
        self.ui.auto_complete_button.toggled.connect(self.update_autocomplete)
        self.ui.headless_checkbox.toggled.connect(self.update_headless_mode)
        self.ui.detach_checkbox.toggled.connect(self.update_detach_mode)
        self.ui.cvv_button.clicked.connect(self.update_cvv)
        self.ui.reset_defaults_button.clicked.connect(self.reset_config)
        self.ui.save_settings_button.clicked.connect(self.save_config)
        self.ui.start_button.clicked.connect(self.request_start)
        self.ui.stop_button.clicked.connect(self.stop_button_functions)

        # Instance variables
        self.current_config = read_config()
        self.page_refresh_count = 0
        self.selected_product = None
        self.ready_to_run = False
        self.thread = None
        self.is_timeout_error = False

        # Set instance default values
        self.update_url_button_display('add')  # Starts with 'Add' URL button visble
        self.ui.tabWidget.setCurrentIndex(0)  # Starts on "Program" tab
        self.ui.chrome_data_path_example.setText(r'eg. C:\Users\YourUser\AppData\Local\Google\Chrome\User Data')
        self.ui.cvv_field.setMaxLength(3)
        self.ui.confirm_reset_warning.setText('')
        self.ui.item_logo.setPixmap(QPixmap('images/hank.png'))  # Sets default display image
        self.ui.selected_product_label.setText('')
        self.ui.start_button.setEnabled(True)
        self.ui.stop_button.setEnabled(False)

        # Prints 'Welcome Message' to GUI console
        self.ui.console_display.clear()
        self.welcome_message = "**Welcome to Pokebot**"
        self.initial_html = markdown.markdown(self.welcome_message)
        self.initial_html = self.initial_html.replace("<p>", "<span>").replace("</p>", "</span>")
        self.initial_html = self.initial_html.strip()
        self.ui.console_display.setHtml(self.initial_html)

        # Set widget values based on config settings
        self.ui.timezone_field.setCurrentText(self.current_config['timezone'])
        self.ui.chrome_data_path_display.setText(self.current_config['selenium_options']['user-data-dir'])
        self.ui.auto_complete_button.setChecked(self.current_config['auto_complete'])
        self.ui.headless_checkbox.setChecked(self.current_config['selenium_options']['headless'])
        self.ui.detach_checkbox.setChecked(self.current_config['selenium_options']['detach'])
        self.ui.chrome_profile_field.setCurrentText(self.current_config['selenium_options']['profile-directory'])
        self.ui.refresh_time_field.setCurrentText(parse_refresh_time(self.current_config['refresh_time']))
        self.ui.max_quantity_field.setCurrentText(str(self.current_config['max_quantity']))
        self.load_product_list()
        if self.current_config['cvv_code'] != '':
            self.ui.cvv_set_indicator.setText(f'Current: {self.current_config["cvv_code"]}')
        else:
            self.ui.cvv_set_indicator.setText('Not Set')
        if self.current_config['auto_complete']:
            self.ui.auto_complete_button.setText('Enabled')
        else:
            self.ui.auto_complete_button.setText('Disabled')


    def print_to_console_display(self, message, timestamp=True):
        # Provides a method for printing to the GUI console display
        if timestamp:
            formatted_message = append_timestamp(self.current_config['timezone'], message)
        else:
            formatted_message = message
        new_html = markdown.markdown(formatted_message)
        current_html = self.ui.console_display.toHtml().strip()
        new_html = new_html.replace("<p>", "<span>").replace("</p>", "</span>")
        new_html = new_html.strip()
        # If content exists, add a single <br> before new content (for spacing)
        if current_html:
            updated_html = current_html + "<br>" + new_html
        else:
            updated_html = new_html  # No extra spacing on first entry
        self.ui.console_display.setHtml(updated_html)
        self.ui.console_display.verticalScrollBar().setValue(self.ui.console_display.verticalScrollBar().maximum())


    def load_product_list(self):
        # Loads list of product names into display field
        for product in self.current_config['saved_products']:
            name = product['name']
            self.ui.product_display_list.addItem(name)


    def set_selected_product(self):
        # Sets the URL to be used when a URL in the list is double clicked
        selected_product = self.ui.product_display_list.selectedItems()[0].text()
        for product in self.current_config['saved_products']:
            if product['name'] == selected_product:
                self.selected_product = product
                self.ui.selected_product_label.setText(product['name'])
                self.update_item_logo(product['image_file_path'])
        self.print_to_console_display(f"Selected Product: **{self.selected_product['name']}**")


    def add_product(self):
        url = self.ui.url_entry_line.text().strip()
        if url:
            new_product = parse_target_url(url)
            if not self.already_in_list(new_product['url']):
                product_name = new_product['name']
                self.ui.product_display_list.addItem(product_name)
                self.current_config['saved_products'].append(new_product)
                self.ui.url_entry_line.clear()


    def already_in_list(self, url) -> bool:
        if not self.current_config['saved_products']:
            return False
        else:
            for product in self.current_config['saved_products']:
                if url == product['url']:
                    self.print_to_console_display('Product already in list')
                    return True
            return False


    def delete_selected_product(self, all=False):
        selected_items = (
            [self.ui.product_display_list.item(i) for i in range(self.ui.product_display_list.count())]
            if all else self.ui.product_display_list.selectedItems()
        )
        if not selected_items:
            return
        for item in selected_items:
            item_name = item.text()
            self.ui.product_display_list.takeItem(self.ui.product_display_list.row(item))
            if item_name == self.ui.selected_product_label.text():
                self.selected_product = None
                self.ui.selected_product_label.setText('')
                self.ready_to_run = False
                self.update_item_logo('images/hank.png')
                self.print_to_console_display('No item selected')
            for product in self.current_config['saved_products']:
                if item_name == product['name']:
                    self.current_config['saved_products'].remove(product)


    def update_url_button_display(self, display_button):
        if display_button == 'add':
            self.ui.add_url_button.raise_()
        else:
            self.ui.remove_url_button.raise_()


    def change_timezone(self):
        selected_timezone = self.ui.timezone_field.currentText()
        if selected_timezone == 'UTC':
            self.current_config['timezone'] = f"{selected_timezone}"
        else:
            self.current_config['timezone'] = str(get_localzone())
        self.ui.confirm_reset_warning.setText('')


    def update_data_path(self):
        usr_data_path_input = self.ui.chrome_data_path_field.text().strip().replace('\\', '/')
        self.ui.chrome_data_path_display.setText(usr_data_path_input)
        self.current_config['selenium_options']['user-data-dir'] = usr_data_path_input
        self.ui.chrome_data_path_field.clear()
        self.ui.confirm_reset_warning.setText('')


    def update_refresh_time(self):
        selected_refresh_time = self.ui.refresh_time_field.currentText()
        selected_refresh_time = parse_refresh_time(selected_refresh_time)
        self.current_config['refresh_time'] = selected_refresh_time
        self.ui.confirm_reset_warning.setText('')


    def update_max_quantity(self):
        selected_max_quantity = self.ui.max_quantity_field.currentText()
        self.current_config['max_quantity'] = selected_max_quantity
        self.ui.confirm_reset_warning.setText('')


    def update_chrome_profile(self):
        selected_chrome_profile = self.ui.chrome_profile_field.currentText()
        self.current_config['selenium_options']['profile-directory'] = selected_chrome_profile
        self.ui.confirm_reset_warning.setText('')


    def update_headless_mode(self):
        headless_state = self.ui.headless_checkbox.isChecked()
        self.current_config['selenium_options']['headless'] = headless_state
        self.ui.confirm_reset_warning.setText('')


    def update_detach_mode(self):
        detach_state = self.ui.detach_checkbox.isChecked()
        self.current_config['selenium_options']['detach'] = detach_state
        self.ui.confirm_reset_warning.setText('')


    def update_cvv(self):
        usr_cvv_code_input = self.ui.cvv_field.text().strip()
        self.current_config['cvv_code'] = usr_cvv_code_input
        if usr_cvv_code_input != '':
            self.ui.cvv_set_indicator.setText(f"Current: {usr_cvv_code_input}")
        else:
            self.ui.cvv_set_indicator.setText('Not Set')
        self.ui.cvv_field.clear()
        self.ui.confirm_reset_warning.setText('')


    def update_autocomplete(self):
        auto_complete_state = self.ui.auto_complete_button.isChecked()
        if auto_complete_state:
            self.ui.auto_complete_button.setText('Enabled')
        else:
            self.ui.auto_complete_button.setText('Disabled')
        self.current_config['auto_complete'] = auto_complete_state
        self.ui.confirm_reset_warning.setText('')


    def reset_config(self):
        self.current_config = read_config(default=True)
        self.ui.timezone_field.setCurrentText('UTC')
        self.ui.cvv_set_indicator.setText('Not Set')
        self.ui.auto_complete_button.setChecked(False)
        self.ui.refresh_time_field.setCurrentText('5 seconds')
        self.ui.max_quantity_field.setCurrentText('1')
        self.ui.chrome_data_path_display.setText('')
        self.ui.chrome_profile_field.setCurrentText('Default')
        self.ui.headless_checkbox.setChecked(False)
        self.ui.detach_checkbox.setChecked(False)
        self.ui.url_entry_line.clear()
        self.delete_selected_product(all=True)
        self.ui.confirm_reset_warning.setText('Press Save Settings \nto confirm -->')


    def save_config(self):
        self.ready_to_run = False
        write_config(self.current_config)
        self.print_to_console_display("Configuration settings saved")
        self.ui.confirm_reset_warning.setText('Settings Saved')


    def external_log(self, message):
        self.print_to_console_display(message)


    def update_counter(self, count):
        self.page_refresh_count = count
        self.ui.refresh_number.display(self.page_refresh_count)


    def update_item_logo(self, image_path):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.ui.item_logo.setPixmap(pixmap)
        else:
            self.print_to_console_display("Failed to load image")


    def request_start(self):
        if not self.ready_to_run:
            self.ready_to_run = self.init_program()
        else:
            self.run_program()


    def init_program(self):
        if not self.selected_product:
            self.print_to_console_display("Error: No product selected")
            return False
        if self.current_config['selenium_options']['user-data-dir'] == '':
            self.print_to_console_display("Error: No Chrome Data Path entered")
            return False

        self.print_to_console_display("Selected settings:")
        self.print_to_console_display(f"Product: **{self.selected_product['name']}**", False)
        self.print_to_console_display(f"URL: **{self.selected_product['url']}**", False)
        self.print_to_console_display(f"Max Quantity: **{self.current_config['max_quantity']}**", False)
        self.print_to_console_display(f"Refresh Time: **{self.current_config['refresh_time']}**", False)
        if self.current_config['cvv_code'] == '':
            self.print_to_console_display("CVV Code: **None**", False)
        else:
            self.print_to_console_display(f"CVV Code: **{self.current_config['cvv_code']}**", False)
        if self.current_config['auto_complete']:
            self.print_to_console_display("Auto-complete: **Enabled**", False)
        else:
            self.print_to_console_display("Auto-complete: **Disabled**", False)
        self.print_to_console_display(
            f"Chrome Data Path: **{self.current_config['selenium_options']['user-data-dir']}**", False)
        self.print_to_console_display(
            f"Chrome Profile: **{self.current_config['selenium_options']['profile-directory']}**", False)

        if self.current_config['selenium_options']['headless']:
            self.print_to_console_display(f"Headless Mode: **Enabled**", False)
        else:
            self.print_to_console_display(f"Headless Mode: **Disabled**", False)

        if self.current_config['selenium_options']['detach']:
            self.print_to_console_display(f"Detached Mode: **Enabled**", False)
        else:
            self.print_to_console_display(f"Detached Mode: **Disabled**", False)

        self.print_to_console_display("Once settings confirmed, press 'START' to begin")
        return True


    def run_program(self):
        program_data = {
            'selected_product': self.selected_product,
            'refresh_time': self.current_config['refresh_time'],
            'max_quantity': self.current_config['max_quantity'],
            'cvv_code': self.current_config['cvv_code'],
            'auto_complete': self.current_config['auto_complete'],
            'selenium_options': self.current_config['selenium_options']
        }
        self.print_to_console_display("Starting program")
        self.comm.running = True
        self.thread = threading.Thread(target=web.main, args=(program_data, self.comm))
        self.thread.start()
        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)


    def stop_program(self):
        if self.thread is not None:
            self.print_to_console_display('Stopping Program')
            self.comm.running = False

            if self.comm.driver is not None:
                self.comm.driver.quit()
                self.comm.driver = None
                self.print_to_console_display('Selenium Driver Closed')

            self.thread = None
            self.ui.start_button.setEnabled(True)
            self.ui.stop_button.setEnabled(False)


    def stop_button_functions(self):
        if self.is_timeout_error:
            self.clear_timeout_error()
        else:
            self.stop_program()


    def activate_timeout_error(self, data):
        self.is_timeout_error = data
        self.clear_timeout_error()


    def clear_timeout_error(self):
        while self.is_timeout_error:
            manual_bypass = input("Enter any text in console, or click STOP to proceed: ")
            if manual_bypass:
                break
            else:
                continue
        self.is_timeout_error = False
        self.print_to_console_display("Timeout Error cleared")





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
