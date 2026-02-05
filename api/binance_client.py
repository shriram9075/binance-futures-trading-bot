from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL

def create_client() -> Client:
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = BASE_URL
    return client
