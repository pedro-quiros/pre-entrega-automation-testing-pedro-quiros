import pytest
from pages.LoginPage import LoginPage
from utils.datos_usuarios import CASOS_LOGIN

@pytest.mark.parametrize("usuario, clave, debe_funcionar", CASOS_LOGIN)
def test_login_parametrizado(driver, usuario, clave, debe_funcionar):
    login_page = LoginPage(driver)
    
    login_page.abrir()
    login_page.completar_usuario(usuario)
    login_page.completar_clave(clave)
    login_page.enviar()
    
    if debe_funcionar:
        # Si las credenciales son válidas, revisamos la URL.
        assert "/inventory.html" in driver.current_url, (
            f"Se esperaba redirigir a /inventory.html pero se quedó en: {driver.current_url}"
        )
    else:
        # Si son inválidas, validamos que permanezca en la página de login y que aparezca un mensaje de error.
        assert login_page.hay_error(), (
            f"Se esperaba un mensaje de error para el usuario '{usuario}', pero no apareció."
        )