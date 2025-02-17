import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


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

    try:
        # Tries adding item to cart, refreshes page based on provided refresh_time if not available
        added_to_cart = try_adding_to_cart(driver, comm, prod_url, prod_id, refresh_time)

        # If the user requests more than 1 item, navigates to the 'cart' page and updates quantity
        quantity_set = update_quantity(driver, comm, req_quant)

        # Placed order on final checkout screen. May auto-complete if user has previously verified CVV
        order_placed = place_order(driver, comm, cvv_code, auto_complete)

        if added_to_cart and quantity_set and order_placed:
            comm.external_log.emit('Order complete. Closing driver')

    finally:
        # Ensure driver is properly closed when script ends
        if driver:
            driver.quit()
            comm.external_log.emit("Driver closed")


def try_adding_to_cart(driver, comm, prod_url, prod_id: str, refresh_time: int) -> bool:
    button_id = f'addToCartButtonOrTextIdFor{prod_id}'
    refresh_count = 0

    driver.get(prod_url)
    comm.external_log.emit('URL Loaded')
    while True:
        try:
            # Locates the 'Add to Cart' button
            add_to_cart_button = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located(
                    (By.ID, button_id)
                )
            )
            if add_to_cart_button.get_attribute('disabled'):
                # Product is out of stock
                if refresh_count < 1:
                    comm.external_log.emit(f"Item out of stock. \
                        Initiating refresh every {refresh_time} seconds")
                    refresh_count += 1
                    time.sleep(refresh_time)
                    driver.refresh()
                    comm.counter_update.emit(i)  # Updates GUI refresh counter
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


def update_quantity(driver, comm, req_quant: str) -> bool:
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
            place_order_button.click()
            comm.external_log.emit("'Place Order' button clicked")

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

        except StaleElementReferenceException:
            comm.external_log.emit("Reloading elements...")
            time.sleep(1)
            continue
        except NoSuchElementException:
            comm.external_log.emit("Attempting to locate elements...")
            time.sleep(1)
            continue
