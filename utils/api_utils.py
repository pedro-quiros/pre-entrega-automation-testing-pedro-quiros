import pytest
import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()

BASE_API_URL = "https://reqres.in"

try:
    MI_API_KEY = os.environ["REQRES_API_KEY"]
    logger.info("API KEY cargada exitosamente desde el archivo .env")
except KeyError:
    raise RuntimeError("Error: La variable REQRES_API_KEY no está definida en el archivo .env")

@pytest.fixture(scope="module")
def api_headers():
    return {
        "Content-Type": "application/json",
        "x-api-key": MI_API_KEY
    }

@pytest.fixture(scope="module")
def api_login_url():
    return f"{BASE_API_URL}/api/login"

@pytest.fixture(scope="module")
def api_users_url():
    return f"{BASE_API_URL}/api/users"