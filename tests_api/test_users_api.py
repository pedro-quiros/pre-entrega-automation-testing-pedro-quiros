import pytest
import requests
import logging  # <-- Importamos el módulo de logs nativo
from utils.api_utils import *

# Configuramos el logger para este archivo
logger = logging.getLogger(__name__)

@pytest.mark.api
def test_get_users_validation(api_users_url, api_headers):
    params = {"page": 1}
    
    logger.info("Iniciando petición GET al endpoint de usuarios...")
    response = requests.get(api_users_url, params=params, headers=api_headers)
    
    logger.info(f"Respuesta recibida con status code: {response.status_code}")
    assert response.status_code == 200, f"Error al consultar usuarios, status: {response.status_code}"
    
    json_data = response.json()
    usuarios = json_data["data"]
    logger.info(f"Se encontraron {len(usuarios)} usuarios para validar.")
    
    for usuario in usuarios:
        # Validamos las claves básicas
        assert "id" in usuario
        assert "email" in usuario
        assert "first_name" in usuario
        assert "last_name" in usuario
        assert "avatar" in usuario
        
        # Validamos el avatar del usuario
        avatar_url = usuario["avatar"]
        assert avatar_url.lower().endswith(".jpg")
        
    logger.info("Todos los usuarios e imágenes .jpg fueron validados con éxito.")