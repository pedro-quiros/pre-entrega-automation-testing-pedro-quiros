from utils.InventoryPage import *

def test_inventory_title(login_in_driver):
	driver = login_in_driver
	titulo = get_title(driver)
	assert titulo == "Swag Labs", "El titulo de la pagina a la que se accede no es correcto"

def test_productos_visibles(login_in_driver):
	driver = login_in_driver
	productos = get_products(driver)
	assert len(productos) > 0

def test_ui_elements(login_in_driver):
	driver = login_in_driver
	menu = get_menu_button(driver)
	filtro = get_sort_dropdown(driver)
	carrito = get_shopping_cart(driver)
	logo = get_app_logo(driver)

	assert menu.is_displayed(), "El icono del menu no está presente en la pagina"
	assert filtro.is_displayed(), "El filtro del catalogo no está presente en la pagina"
	assert carrito.is_displayed(), "El icono del carrito no está presente en la pagina"
	assert logo.is_displayed(), "El logo de la aplicacion no está presente en la pagina"