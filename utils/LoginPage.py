from selenium.webdriver.common.by import By

def login(driver):
    driver.get("https://www.saucedemo.com/")

    usuario = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    boton = driver.find_element(By.ID, "login-button")

    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")
    boton.click()