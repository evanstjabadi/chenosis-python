from http import HTTPStatus
from pytest_httpx import HTTPXMock
import pytest

from chenosis.client import ChenosisClient
from chenosis.exceptions import InvalidCredentials

    
def test_authentication_success(httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        status_code=HTTPStatus.OK,
        url="http://testing.chenosis.io/oauth/client?grant_type=client_credentials", 
        json={
            "access_token": "short-lived-token"
        }
    )
    
    host = "http://testing.chenosis.io"
    client_id = "TEST_CLIENT_ID"
    client_secret = "TEST_CLIENT_SECRET"
    
    chenosis_client = ChenosisClient(
        host=host,
        client_id=client_id,
        client_secret=client_secret
    )
    
    assert chenosis_client.get_access_token() == "short-lived-token"
    
def test_authentication_incorrect_credentials(httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        status_code=HTTPStatus.UNAUTHORIZED,
        url="http://testing.chenosis.io/oauth/client?grant_type=client_credentials", 
        json={
            "error": "incorrect combination of credentials"
        }
    )
    
    host = "http://testing.chenosis.io"
    client_id = "BAD_CLIENT_ID"
    client_secret = "BAD_CLIENT_SECRET"
    
    with pytest.raises(InvalidCredentials):
        _ = ChenosisClient(
            host=host,
            client_id=client_id,
            client_secret=client_secret
        )
