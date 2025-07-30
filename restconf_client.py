# restconf_client.py
import requests
from requests.auth import HTTPBasicAuth

class RestconfClient:
    def __init__(self, host, user, password):
        self.base_url = f"https://{host}/restconf/data"
        self.auth = HTTPBasicAuth(user, password)
        self.headers = {
            "Content-Type": "application/yang-data+json",
            "Accept": "application/yang-data+json"
        }

    def get(self, endpoint):
        response = requests.get(
            f"{self.base_url}/{endpoint}",
            auth=self.auth,
            headers=self.headers,
            verify=False
        )
        return response

    def patch(self, endpoint, payload):
        response = requests.patch(
            f"{self.base_url}/{endpoint}",
            json=payload,
            auth=self.auth,
            headers=self.headers,
            verify=False
        )
        return response

    def post(self, endpoint, payload):
        response = requests.post(
            f"{self.base_url}/{endpoint}",
            json=payload,
            auth=self.auth,
            headers=self.headers,
            verify=False
        )
        return response
    
    def put(self, endpoint, payload):
        response = requests.put(
            f"{self.base_url}/{endpoint}",
            json=payload,
            auth=self.auth,
            headers=self.headers,
            verify=False
        )
        response.raise_for_status()
        return response
