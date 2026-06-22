import pytest
import requests
from utils.api_utils import *

# Los datos tienen que ser EXACTAMENTE estos para que ReqRes te dé un 200
CASOS_API_LOGIN = [
    ({"email": "eve.holt@reqres.in", "password": "cityslickka"}, 200, True),
    ({"email": "eve.holt@reqres.in"}, 400, False)
]

@pytest.mark.api
@pytest.mark.parametrize("payload, esperado_status, verificar_token", CASOS_API_LOGIN)
def test_login_parametrizado(api_login_url, api_headers, payload, esperado_status, verificar_token):
    response = requests.post(api_login_url, json=payload, headers=api_headers)
    
    assert response.status_code == esperado_status, (
        f"Se esperaba status {esperado_status} pero se obtuvo {response.status_code}"
    )