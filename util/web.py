import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException


def init_driver(selenium_options):
    """Initializes and returns a Selenium WebDriver instance."""
    driver_path = chromedriver_autoinstaller.install()
    service = Service(driver_path)

    options = webdriver.ChromeOptions()
    if selenium_options['user-data-dir'] != '':
        options.add_argument(f"--user-data-dir={selenium_options['user-data-dir']}")
    if selenium_options['profile-directory'] != '':
        options.add_argument(f"--profile-directory={selenium_options['profile-directory']}")
    if selenium_options['headless']:
        options.add_argument("--headless")
    if selenium_options['detach']:
        options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(10)
    return driver


def main(program_data, comm):
    # Parse program variables
    req_quant = program_data['max_quantity']
    refresh_time = program_data['refresh_time']
    cvv_code = program_data['cvv_code']
    auto_complete = program_data['auto_complete']

    selected_prod = program_data['selected_product']
    prod_url = selected_prod['url']
    prod_id = selected_prod['id']

    selenium_options = program_data['selenium_options']

    driver = init_driver(selenium_options)
    comm.driver = driver

    order_complete = False

    try:
        while comm.running and not order_complete:

            comm.external_log.emit('Trying to add to cart')
            adding_to_cart_result = try_adding_to_cart(driver, comm, prod_url, refresh_time)
            comm.external_log.emit(f"Add to cart result: {adding_to_cart_result}")

            comm.external_log.emit('Trying to update quantity')
            update_quantity_result = update_quantity(driver, comm, req_quant)
            comm.external_log.emit(f"Update Quantity result: {update_quantity_result}")

            comm.external_log.emit('Trying to place order')
            place_order_result = place_order(driver, comm, cvv_code, auto_complete)
            comm.external_log.emit(f"Place Order result: {place_order_result}")

            comm.external_log.emit('Order completed. web.main exiting')
            if adding_to_cart_result and update_quantity_result and place_order_result:
                order_complete = True

    finally:
        if driver:
            comm.external_log.emit('Web.main closing driver and exiting')
            driver.quit()
            comm.driver = None


def try_adding_to_cart(driver, comm, prod_url, refresh_time: int) -> bool:
    refresh_count = 0

    driver.get(prod_url)
    comm.external_log.emit('URL Loaded')
    while True:
        time.sleep(0.5)
        try:
            # Locates the 'Add to Cart' button
            add_to_cart_button = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.XPATH, '//button[text()="Add to cart"]')
                )
            )
            if add_to_cart_button.get_attribute('disabled'):
                # Product is out of stock
                if refresh_count < 1:
                    comm.external_log.emit(f"Item out of stock. Initiating refresh every {refresh_time} seconds")

                refresh_count += 1
                time.sleep(refresh_time)
                driver.refresh()
                comm.counter_update.emit(refresh_count)  # Updates GUI refresh counter
                continue

            else:
                # Adds item to cart
                add_to_cart_button.click()
                comm.external_log.emit('Item added to cart')
                time.sleep(1)
                return True

        except StaleElementReferenceException:
            comm.external_log.emit("Reloading 'Add to Cart' button...")
            time.sleep(1)
            continue
        except NoSuchElementException:
            comm.external_log.emit("Attempting to locate 'Add to Cart' button...")
            time.sleep(1)
            continue
        except TimeoutException:
            comm.external_log.emit("Add to Cart Button Timeout. Refreshing...")
            driver.refresh()
            time.sleep(2)
            continue


def update_quantity(driver, comm, req_quant: str) -> bool:
    if req_quant == '1':
        return True
    driver.get('https://www.target.com/cart')
    int_quantity = int(req_quant)
    while True:
        try:
            # Tried to locate and select quantity button
            quantity_select_element = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.CSS_SELECTOR, 'select[data-test="cartItem-qty"]')
                )
            )
            selected_element = Select(quantity_select_element)
            available_values = [option.get_attribute('value') for option in selected_element.options]

            while int_quantity > 0:
                if req_quant in available_values:
                    selected_element.select_by_value(req_quant)
                    comm.external_log.emit(f'Quantity selected: {req_quant}')
                    time.sleep(1)
                    return True
                else:
                    comm.external_log.emit(f"Quantity: {req_quant} not available")
                    int_quantity = int_quantity - 1
                    req_quant = str(int_quantity)
                    comm.external_log.emit(f"Retrying with quantity: {req_quant}")
                    continue
            comm.external_log.emit('Error: Unable to select quantity')
            return False

        except StaleElementReferenceException:
            comm.external_log.emit("Reloading 'Quantity Selector'...")
            time.sleep(1)
            continue
        except NoSuchElementException:
            comm.external_log.emit("Attempting to locate 'Quantity Selector'...")
            time.sleep(1)
            continue
        except TimeoutException:
            comm.external_log.emit("Quantity Selector Timeout. Refreshing...")
            driver.refresh()
            time.sleep(2)
            continue


def place_order(driver, comm, cvv_code: str, auto_complete: bool):
    # Navigates to checkout page
    driver.get('https://www.target.com/checkout')

    # If Auto-complete is enabled, finishes the purchase
    while auto_complete:
        try:
            # Presses place order button
            place_order_button = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.CSS_SELECTOR, 'button[data-test="placeOrderButton"]')
                )
            )
            if place_order_button.get_attribute('disabled'):
                # Save and Continue needs to be pressed
                save_and_continue_button = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.XPATH, '//button[text()="Save and continue]')
                    )
                )
                if save_and_continue_button.get_attribute('disabled'):
                    pass
                else:
                    save_and_continue_button.click()
            place_order_button.click()
            comm.external_log.emit("'Place Order' button clicked")
            try:
                # Enters CVV code into field
                cvv_input = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.ID, 'enter-cvv')
                    )
                )
                cvv_input.send_keys(cvv_code)
                comm.external_log.emit("CVV Code Entered")

                # Locates confirm button and clicks
                confirm_button = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located(
                        (By.CSS_SELECTOR, 'button[data-test="confirm-button"]')
                    )
                )
                confirm_button.click()
                comm.external_log.emit("Order placed successfully!")
                return True
            except TimeoutException:
                comm.external_log.emit('Cannot locate CVV field or confirm button. Assuming order placed')
                return True

        except StaleElementReferenceException:
            comm.external_log.emit("Reloading elements...")
            time.sleep(1)
            continue
        except NoSuchElementException:
            comm.external_log.emit("Attempting to locate elements...")
            time.sleep(1)
            continue
        except TimeoutException:
            comm.external_log.emit("Place Order Button Timeout. Refreshing...")
            driver.refresh()
            time.sleep(2)
            continue
