from .http_client import HttpClient
from .api.users import Users
from .api.trans import Trans
from .api.nodes import Nodes


class Client():
    """Handles configuration and requests to the SynapsePay API.
    """

    def __init__(self, **kwargs):
        """Create a new API client.

        Args:
            client_id (str): your API client id
            client_secret (str): your API client secret
            fingerprint (str): the user's fingerprint
            ip_address (str): the user's IP address
            development_mode (bool): if True, requests sent to sandbox
            endpoints (else production)
            logging (bool): if True, requests logged to stdout

        Todo:
            Allow logging to file
        """
        base_url = 'https://synapsepay.com/api/3'
        if kwargs.get('development_mode'):
            base_url = 'https://sandbox.synapsepay.com/api/3'

        self.http_client = HttpClient(base_url=base_url, **kwargs)
        self.users = Users(self.http_client)
        self.nodes = Nodes(self.http_client)
        self.trans = Trans(self.http_client)
