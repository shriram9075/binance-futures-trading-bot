import argparse
import os
from dotenv import load_dotenv
from binance.client import Client
from logger import setup_logger

# Load .env
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Initialize logger
logger = setup_logger()

# Initialize Binance Testnet client
client = Client(API_KEY, API_SECRET, testnet=True)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True, type=str, help="Trading symbol e.g. BTCUSDT")
    parser.add_argument("--side", required=True, type=str, choices=["BUY", "SELL"], help="BUY or SELL")
    parser.add_argument("--type", required=True, type=str, choices=["MARKET", "LIMIT"], help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT order)")
    args = parser.parse_args()

    # Validate LIMIT price
    if args.type == "LIMIT" and not args.price:
        logger.error("Price is required for LIMIT orders")
        print("Error: Price is required for LIMIT orders")
        return

    order_params = {
        "symbol": args.symbol,
        "side": args.side,
        "type": args.type,
        "quantity": args.quantity
    }

    if args.type == "LIMIT":
        order_params["price"] = args.price
        order_params["timeInForce"] = "GTC"

    logger.info(f"Order Request: {order_params}")
    print(f"Placing order: {order_params}")

    try:
        order = client.futures_create_order(**order_params)
        logger.info(f"Order Response: {order}")
        print(f"Order placed successfully! Order ID: {order['orderId']}")
    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        print(f"Order failed: {str(e)}")

if __name__ == "__main__":
    main()
