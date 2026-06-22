from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class InventoryPage:
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    _SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    _APP_LOGO = (By.CLASS_NAME, "app_logo")
    _ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    _REMOVE_BUTTONS = (By.CLASS_NAME, "btn_secondary") 
    _FIRST_PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        return self.driver.title

    def obtener_cantidad_productos(self):
        self.wait.until(EC.visibility_of_element_located(self._PRODUCTS))
        return len(self.driver.find_elements(*self._PRODUCTS))

    def abrir_menu_lateral(self):
        self.wait.until(EC.element_to_be_clickable(self._MENU_BUTTON)).click()
        return self

    def obtener_texto_logo(self):
        return self.wait.until(EC.visibility_of_element_located(self._APP_LOGO)).text

    def agregar_primer_producto_al_carrito(self):
        botones = self.wait.until(EC.presence_of_all_elements_located(self._ADD_TO_CART_BUTTONS))
        botones[0].click()
        return self

    def remover_primer_producto_del_carrito(self):
        botones_remover = self.wait.until(EC.presence_of_all_elements_located(self._REMOVE_BUTTONS))
        botones_remover[0].click()
        return self

    def ordenar_por_valor(self, valor):
        dropdown_elemento = self.wait.until(EC.visibility_of_element_located(self._SORT_DROPDOWN))
        select = Select(dropdown_elemento)
        select.select_by_value(valor)
        return self
    
    def obtener_nombre_primer_producto(self):
        elementos = self.wait.until(EC.presence_of_all_elements_located(self._FIRST_PRODUCT_NAME))
        return elementos[0].text

    def ir_al_carrito(self):
        self.driver.find_element(*self._SHOPPING_CART).click()