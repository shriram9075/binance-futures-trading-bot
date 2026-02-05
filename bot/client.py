import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from config import BINANCE_API_KEY, BINANCE_API_SECRET, BASE_URL

class BinanceFuturesClient:
    def __init__(self):
        if not BINANCE_API_KEY or not BINANCE_API_SECRET:
            raise RuntimeError("API keys not set")

    def _sign(self, params: dict) -> dict:
        query_string = urlencode(params)
        signature = hmac.new(
            BINANCE_API_SECRET.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def place_order(self, params: dict):
        params["timestamp"] = int(time.time() * 1000)
        signed_params = self._sign(params)

        headers = {
            "X-MBX-APIKEY": BINANCE_API_KEY
        }

        response = requests.post(
            f"{BASE_URL}/fapi/v1/order",
            headers=headers,
            params=signed_params,
            timeout=10
        )

        response.raise_for_status()
        return response.json()
