from utils.CartPage import *

def test_cart(login_in_driver):
	driver = login_in_driver

	get_add_to_cart_buttons(driver)[0].click()
	
	contador_cart = get_cart_badge(driver)
	assert contador_cart.text == "1", "La cantidad de productos no se agregaron correctamente"
	
	product_name = get_first_product_name(driver)
	
	click_cart_link(driver)
	
	cart_item = get_cart_item_name(driver)
	assert cart_item == product_name, "El producto agregado no coincide"
    
