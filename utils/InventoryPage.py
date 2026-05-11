from selenium.webdriver.common.by import By

def get_title(driver):
    return driver.title

def get_products(driver):
    return driver.find_elements(By.CLASS_NAME, "inventory_item")

def get_menu_button(driver):
    return driver.find_element(By.ID, "react-burger-menu-btn")

def get_sort_dropdown(driver):
    return driver.find_element(By.CLASS_NAME, "product_sort_container")

def get_shopping_cart(driver):
    return driver.find_element(By.CLASS_NAME, "shopping_cart_link")

def get_app_logo(driver):
    return driver.find_element(By.CLASS_NAME, "app_logo")