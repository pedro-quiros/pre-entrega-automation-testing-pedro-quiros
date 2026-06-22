from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_contador_carrito(self):
        try:
            badge = self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
            return int(badge.text)
        except:
            return 0

    def obtener_nombre_primer_producto(self):
        elementos = self.wait.until(EC.presence_of_all_elements_located(self._ITEM_NAME))
        return elementos[0].text