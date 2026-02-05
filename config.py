import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise EnvironmentError("Missing Binance API credentials")

BASE_URL = "https://testnet.binancefuture.com"