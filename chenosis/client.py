from functools import lru_cache
from typing import Any, Dict
import httpx

from chenosis.exceptions import InvalidCredentials

class ChenosisClient:
    """
    A synchronous REST client for MTN Chenosis APIs
    """
    host: str = None
    client_id: str = None
    client_secret: str = None
    access_token: str = None
    authentication_response: Dict[str, Any] = None
    
    def __init__(self, host: str,  client_id: str, client_secret: str) -> None:
        self.host = host
        self.authentication_response = self.authenticate(client_id=client_id, client_secret=client_secret)
    
    @lru_cache
    def authenticate(self, client_id: str, client_secret: str) -> str:
        authentication_path = "/client-credentials/accesstoken"
        url = self.host+authentication_path
        
        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }
        
        params = {
            "grant_type": "client_credentials"
        }
        
        data = {
            "client_id": client_id,
            "client_secret": client_secret
        }
        
        response = httpx.post(url=url, headers=headers, params=params, data=data)
        
        if not response.is_success:
            raise InvalidCredentials(response.text or response.json())
        
        return response.json()