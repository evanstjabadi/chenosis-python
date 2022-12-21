from functools import lru_cache
from typing import Any, Dict

import httpx

from chenosis.exceptions import InvalidCredentials


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
        authentication_path = "/oauth/client"
        url = self.host + authentication_path

        headers = {"content-type": "application/x-www-form-urlencoded"}

        params = {"grant_type": "client_credentials"}

        data = {"client_id": client_id, "client_secret": client_secret}

        response = httpx.post(url=url, headers=headers, params=params, data=data)

        if not response.is_success:
            raise InvalidCredentials(response.text or response.json())

        return response.json()

    def get_access_token(self) -> str:
        return self.authentication_response["access_token"]
