import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage

@pytest.fixture
def driver():
    """Fixture básico que inicializa y cierra el navegador de forma limpia."""
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    """Fixture que reutiliza el driver para pruebas que asumen sesión iniciada."""
    login_page = LoginPage(driver)
    login_page.abrir().completar_usuario("standard_user").completar_clave("secret_sauce")
    login_page.enviar()
    return driver


# =======================================================
# 📸 CAPTURA DE PANTALLA AUTOMÁTICA EN ERRORES UI
# =======================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura la pantalla en formato Base64 si la prueba de UI falla."""
    import pytest_html
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        if "driver" in item.fixturenames:
            driver_fixture = item.funcargs["driver"]
            screenshot = driver_fixture.get_screenshot_as_base64()
            html_img = f'<div><img src="data:image/png;base64,{screenshot}" alt="screenshot" style="width:600px;height:auto;border: 2px solid #e74c3c; border-radius: 4px;" class="screenshot"/></div>'
            extra.append(pytest_html.extras.html(html_img))
            report.extra = extra


# =======================================================
# 📊 PERSONALIZACIÓN DEL REPORTE (HTML & METADATOS)
# =======================================================

def pytest_html_report_title(report):
    """Configura el título de la pestaña del navegador"""
    report.title = "Reporte de Automatización - Suite Híbrida"

def pytest_html_results_summary(prefix, summary, postfix):
    """Inserta el encabezado principal usando HTML nativo simplificado"""
    prefix.extend([
        "<h1>Resultados de Ejecución de Pruebas Automatizadas</h1>",
        "<p><strong>Descripción:</strong> Suite de pruebas híbrida orientada a la verificación de flujos críticos de la interfaz de usuario (Frontend) y comportamiento de endpoints (Backend).</p>",
        "<p><strong>Automatizador:</strong> Pedro Quirós</p><br>"
    ])

def pytest_metadata(metadata):
    """Estructura la tabla de información general de tu entrega"""
    metadata["Proyecto / Entrega"] = "Proyecto Final - Talento Tech #26143"
    metadata["Automatizador"] = "Pedro Quirós"
    metadata["Aplicación bajo prueba"] = "SauceDemo & ReqRes API"
    metadata["Entorno"] = "QA Testing Local"
    
    # Limpieza de datos nativos redundantes
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)


# =======================================================
# 🎨 DISEÑO VISUAL (ESTILOS CSS)
# =======================================================
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Inyecta CSS embebido para modernizar el diseño del reporte"""
    html_plugin = config.pluginmanager.getplugin("html")
    if html_plugin:
        config._html_css = """
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8f9fa; color: #2c3e50; }
            h1 { color: #1a252f; border-bottom: 3px solid #2c3e50; padding-bottom: 12px; margin-top: 20px; }
            #environment { border: 1px solid #dcdde1; border-radius: 4px; }
            #environment td { padding: 10px; font-size: 14px; }
            #environment tr:nth-child(even) { background-color: #f2f2f2; }
            th { background-color: #2c3e50 !important; color: white !important; font-weight: 600; padding: 12px !important; }
            .passed { background-color: #2ecc71 !important; color: white !important; font-weight: bold; text-align: center; }
            .failed { background-color: #e74c3c !important; color: white !important; font-weight: bold; text-align: center; }
            .skipped { background-color: #f1c40f !important; color: #2c3e50 !important; text-align: center; }
            .sortable { background-color: #34495e; color: white; }
        """