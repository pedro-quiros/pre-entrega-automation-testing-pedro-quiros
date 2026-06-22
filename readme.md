# Proyecto Final QA Automation — Talento Tech #26143

Framework de automatización híbrido diseñado para la ejecución de pruebas funcionales de interfaz de usuario (Frontend) y verificación de endpoints (Backend).

**Automatizador:** Pedro Quirós
**Entorno:** QA / Testing Local
**Aplicaciones bajo prueba:** [SauceDemo (Web)](https://www.saucedemo.com/) & [ReqRes (API)](https://reqres.in/)

---

## Tecnologías y Dependencias
- **Lenguaje de Programación:** Python
- **Automatización UI:** Selenium WebDriver
- **Automatización API:** Requests
- **Core de Testing:** Pytest
- **Reportabilidad:** pytest-html (v4.0+)
- **Seguridad:** python-dotenv

---

## Estructura del Proyecto

El framework implementa el patrón **Page Object Model (POM)** para la capa UI y una arquitectura modular de utilidades para servicios.

```
├── pages/               # Clases de Objetos de Página (POM - UI)
│   ├── LoginPage.py
│   ├── InventoryPage.py
│   └── CartPage.py
├── test/                # Casos de prueba funcionales de UI
├── tests_api/           # Casos de prueba de endpoints e integración (API)
├── utils/               # Módulos auxiliares y gestión de variables
│   ├── api_utils.py
│   └── datos_usuarios.py
├── .env                 # Credenciales locales (excluido de Git)
├── conftest.py          # Fixtures globales, hooks de reporte y screenshots
└── pytest.ini           # Configuración centralizada de Pytest y logs
```

---

## Configuración de Variables de Entorno

Para proteger las credenciales y evitar exponerlas en repositorios públicos, el framework utiliza `python-dotenv`.

En la raíz del proyecto, asegurate de que exista un archivo llamado exactamente `.env` con el siguiente contenido:

```plaintext
REQRES_API_KEY=free_user_XXXXXXXXXXXX
```

> **Importante:** no uses comillas ni espacios alrededor del signo `=`.

---

## Ejecución de Pruebas

### Suite completa (UI + API)

Ejecuta de forma secuencial todo el catálogo de pruebas del framework:

```bash
pytest test/ tests_api/ -vs
```

### Solo pruebas de UI

Filtra y ejecuta únicamente los flujos de Selenium sobre SauceDemo:

```bash
pytest -m ui -vs
```

### Solo pruebas de API

Filtra y ejecuta únicamente los tests de integración sobre los endpoints de ReqRes:

```bash
pytest -m api -vs
```

### Smoke Tests

Ejecuta los flujos críticos del negocio (compras exitosas, validación base de usuarios, etc.):

```bash
pytest -m smoke -vs
```