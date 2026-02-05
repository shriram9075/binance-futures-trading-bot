import os

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

BASE_URL = os.getenv(
    "BASE_URL",
    "https://testnet.binancefuture.com"
)

if not BINANCE_API_KEY or not BINANCE_API_SECRET:
    raise EnvironmentError("Missing Binance API credentials")

