from functools import lru_cache
from typing import Any, Dict

import httpx

from chenosis.exceptions import ChenosisAPIError, InvalidCredentials


class ChenosisClient:
    """
    A synchronous REST client for MTN Chenosis APIs
    """

    authentication_response: Dict[str, Any] = {}

    def __init__(self, host: str, client_id: str, client_secret: str) -> None:
        self.host = host
        self.authentication_response = self.authenticate(
            client_id=client_id, client_secret=client_secret
        )

    @lru_cache
    def authenticate(self, client_id: str, client_secret: str) -> Dict:
        authentication_path = "/oauth/client/accesstoken"
        url = self.host + authentication_path

        headers = {"content-type": "application/x-www-form-urlencoded"}

        params = {"grant_type": "client_credentials"}

        data = {"client_id": client_id, "client_secret": client_secret}

        response = httpx.post(url=url, headers=headers, params=params, data=data)

        if response.is_error:
            raise InvalidCredentials(response.text or response.json())

        return response.json()

    def get_access_token(self) -> str:
        return self.authentication_response["access_token"]

    def get_network_information(self, phone_number: str) -> Dict:
        """
        Retrieve network related information of subscriber as identified by phoneNumber.
        """
        path = f"/mobile/subscriber/{phone_number}/home-location"
        url = self.host + path

        access_token = self.get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}

        response = httpx.get(url=url, headers=headers)

        if response.is_error:
            raise ChenosisAPIError(response.text or response.json())

        return response.json()

    def get_mobile_carrier_details(self, phone_number: str) -> Dict:
        """
        Retrieve mobile carrier details of subscriber as identified by phoneNumber.
        """
        path = f"/{phone_number}/verify"
        url = self.host + path

        access_token = self.get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}

        response = httpx.get(url=url, headers=headers)

        if response.is_error:
            raise ChenosisAPIError(response.text or response.json())

        return response.json()
