import pytest
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from selenium.webdriver.common.by import By

@pytest.mark.ui
@pytest.mark.smoke
def test_flujo_agregar_al_carrito(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.abrir().completar_usuario("standard_user").completar_clave("secret_sauce")
    login_page.enviar()
    
    assert "inventory.html" in driver.current_url
    inventory_page.agregar_primer_producto_al_carrito()
    inventory_page.ir_al_carrito()
    
    assert "cart.html" in driver.current_url
    assert cart_page.obtener_contador_carrito() == 1
    assert len(cart_page.obtener_nombre_primer_producto()) > 0


@pytest.mark.ui
@pytest.mark.regression
def test_remover_producto_desde_inventario(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.abrir().completar_usuario("standard_user").completar_clave("secret_sauce")
    login_page.enviar()
    
    # Agregamos y removemos inmediatamente
    inventory_page.agregar_primer_producto_al_carrito()
    inventory_page.remover_primer_producto_del_carrito()
    
    # Vamos al carrito a confirmar que quedó en 0
    inventory_page.ir_al_carrito()
    assert cart_page.obtener_contador_carrito() == 0, "El contador del carrito debería haber vuelto a 0"


@pytest.mark.ui
@pytest.mark.regression
def test_ordenar_productos_por_nombre_descendente(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    login_page.abrir().completar_usuario("standard_user").completar_clave("secret_sauce")
    login_page.enviar()
    
    # Ordenamos el catálogo de la Z a la A
    inventory_page.ordenar_por_valor("za")
    
    primer_producto_nombre = inventory_page.obtener_nombre_primer_producto()
    
    assert primer_producto_nombre == "Test.allTheThings() T-Shirt (Red)", (
        f"El ordenamiento falló. Se esperaba la remera roja pero se encontró: '{primer_producto_nombre}'"
    )

@pytest.mark.ui
@pytest.mark.regression
def test_bloqueo_acceso_anonimo_a_inventario(driver):
    login_page = LoginPage(driver)
    
    # Forzamos la URL sin loguearnos
    driver.get("https://www.saucedemo.com/inventory.html")
    
    assert login_page.hay_error(), "No se mostró el cartel de error de seguridad al intentar entrar sin credenciales"