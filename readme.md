## [Talento Tech] Pre-Entrega de Proyecto - SauceDemo

Automatización de pruebas web sobre [saucedemo.com](https://www.saucedemo.com/) con Python, Selenium WebDriver y Pytest.

### Tecnologías

- Python
- Pytest
- Selenium WebDriver
- pytest-html

### Estructura

- `test/`: casos de prueba
- `utils/`: funciones auxiliares
- `conftest.py`: fixtures compartidos

### Instalación

```bash
pip install -r requirements.txt
```

### Ejecución

```bash
py -m pytest -v
```

### Reporte HTML

```bash
py -m pytest -v --html=report.html --self-contained-html
```

### Casos cubiertos

- Login con usuario válido
- Verificación del catálogo
- Agregar producto al carrito y validarlo