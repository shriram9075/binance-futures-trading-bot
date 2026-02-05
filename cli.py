import argparse
from bot.validators import validate_order
from bot.orders import OrderService
from bot.logging_config import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_order(args)
        logger = setup_logger(
            "market_order.log" if args.type == "MARKET" else "limit_order.log"
        )

        logger.info(f"Order Request: {vars(args)}")

        service = OrderService()
        response = service.submit(
            args.symbol, args.side, args.type, args.quantity, args.price
        )

        logger.info(f"Order Response: {response}")

        print("\nOrder placed successfully")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Average Price:", response.get("avgPrice", "N/A"))

    except Exception as e:
        print("ERROR:", str(e))

if __name__ == "__main__":
    main()
