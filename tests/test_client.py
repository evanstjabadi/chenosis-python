from http import HTTPStatus
from unittest import mock

import pytest
from pytest_httpx import HTTPXMock

from chenosis.client import ChenosisClient
from chenosis.exceptions import ChenosisAPIError, InvalidCredentials

host = "http://testing.chenosis.io"
client_id = "TEST_CLIENT_ID"
client_secret = "TEST_CLIENT_SECRET"
phone_number = "27723456789"


def test_authentication_success(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        status_code=HTTPStatus.OK,
        url=f"{host}/oauth/client?grant_type=client_credentials",
        json={"access_token": "short-lived-token"},
    )

    chenosis_client = ChenosisClient(
        host=host, client_id=client_id, client_secret=client_secret
    )

    assert chenosis_client.get_access_token() == "short-lived-token"


def test_authentication_incorrect_credentials(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        status_code=HTTPStatus.UNAUTHORIZED,
        url=f"{host}/oauth/client?grant_type=client_credentials",
        json={"error": "incorrect combination of credentials"},
    )

    client_id = "BAD_CLIENT_ID"
    client_secret = "BAD_CLIENT_SECRET"

    with pytest.raises(InvalidCredentials):
        _ = ChenosisClient(host=host, client_id=client_id, client_secret=client_secret)


def test_get_access_token() -> None:
    with mock.patch("chenosis.client.ChenosisClient.authenticate") as mock_authenticate:
        mock_authenticate.return_value = {"access_token": "short-lived-token"}

        chenosis_client = ChenosisClient(
            host=host, client_id=client_id, client_secret=client_secret
        )

        assert chenosis_client.get_access_token() == "short-lived-token"


def test_get_network_information(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        status_code=HTTPStatus.OK,
        url=f"{host}/mobile/subscriber/{phone_number}/home-location",
        json={"data": {"country": "SA"}},  # TODO: Put correct information
    )

    with mock.patch("chenosis.client.ChenosisClient.authenticate") as mock_authenticate:
        mock_authenticate.return_value = {"access_token": "short-lived-token"}

        chenosis_client = ChenosisClient(
            host=host, client_id=client_id, client_secret=client_secret
        )

        response = chenosis_client.get_network_information(phone_number=phone_number)

        assert response == {"data": {"country": "SA"}}  # TODO: Put correct information


def test_get_network_information_raise_error(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        status_code=HTTPStatus.SERVICE_UNAVAILABLE,
        url=f"{host}/mobile/subscriber/{phone_number}/home-location",
        json={"error": "Service Unavailable"},
    )

    with mock.patch("chenosis.client.ChenosisClient.authenticate") as mock_authenticate:
        mock_authenticate.return_value = {"access_token": "short-lived-token"}

        chenosis_client = ChenosisClient(
            host=host, client_id=client_id, client_secret=client_secret
        )

        with pytest.raises(ChenosisAPIError):
            _ = chenosis_client.get_network_information(phone_number=phone_number)


def test_get_mobile_carrier_details(httpx_mock: HTTPXMock) -> None:
    httpx_mock.add_response(
        status_code=HTTPStatus.OK,
        url=f"{host}/{phone_number}/verify",
        json={"data": {"country": "SA"}},  # TODO: Put correct information
    )

    with mock.patch("chenosis.client.ChenosisClient.authenticate") as mock_authenticate:
        mock_authenticate.return_value = {"access_token": "short-lived-token"}

        chenosis_client = ChenosisClient(
            host=host, client_id=client_id, client_secret=client_secret
        )

        response = chenosis_client.get_mobile_carrier_details(phone_number=phone_number)

        assert response == {"data": {"country": "SA"}}  # TODO: Put correct information
