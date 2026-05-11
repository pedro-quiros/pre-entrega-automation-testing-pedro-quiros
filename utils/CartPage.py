from selenium.webdriver.common.by import By

def get_add_to_cart_buttons(driver):
    return driver.find_elements(By.CLASS_NAME, "btn_inventory")

def get_cart_badge(driver):
    return driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

def get_first_product_name(driver):
    return driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

def click_cart_link(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

def get_cart_item_name(driver):
    return driver.find_element(By.CLASS_NAME, "inventory_item_name").text