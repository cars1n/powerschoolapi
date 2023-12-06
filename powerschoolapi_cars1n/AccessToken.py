import requests
import base64
import ssl
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context
import os
from dotenv import load_dotenv

# Load environment variables from .env file just once
load_dotenv()

class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context()
        context.options &= ~ssl.OP_NO_TLSv1_1
        kwargs['ssl_context'] = context
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

class AccessToken:
    def __init__(self):
        self.powerschool_server_url = os.environ.get('POWERSCHOOL_SERVER_URL')
        self.client_id = os.environ.get('CLIENT_ID')
        self.client_secret = os.environ.get('CLIENT_SECRET')
        self.token = None
        self.session = requests.Session()
        self.session.mount("https://", TLSAdapter())

    def _encode_credentials(self):
        # Encodes the client_id and client_secret
        credentials = f"{self.client_id}:{self.client_secret}"
        return base64.b64encode(credentials.encode()).decode()

    def get_access_token(self):
        if not self.token:
            headers = {
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Authorization": f"Basic {self._encode_credentials()}"
            }
            data = {"grant_type": "client_credentials"}
            url = f"{self.powerschool_server_url}/oauth/access_token"

            response = self.session.post(url, headers=headers, data=data)

            if response.status_code == 200:
                self.token = response.json()["access_token"]
            else:
                raise Exception(f"Failed to obtain access token. Status Code: {response.status_code}, Message: {response.text}")

        return self.token
