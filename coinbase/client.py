import requests

BASE_URL = "https://api.coinbase.com"

class HTTPBadResponse(RuntimeError):
    pass

class BadResponse(RuntimeError):
    pass

class Client:
    def __init__(self, base_url=BASE_URL, timeout=10):
        self.base_url = base_url
        self.timeout = timeout # seconds

    def get_currencies(self):
        full_url = f"{self.base_url}/v2/currencies"

        try:
            resp = requests.get(full_url, timeout=self.timeout)
            resp.raise_for_status()
            return resp
        except requests.exceptions.HTTPError as http_err:
            raise HTTPBadResponse(f"HTTP BadResponse, code: {http_err.response.status_code}, body: {http_err.response.text}")
        except Exception as err:
            raise BadResponse(f"BadResponse, error: {err}")
