import argparse
from bot.validators import validate_order
from bot.orders import OrderService
from bot.logging_config import setup_logger


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # Validate input
        validate_order(args)

        # Setup logger
        log_file = "market_order.log" if args.type == "MARKET" else "limit_order.log"
        logger = setup_logger(log_file)

        # Pretty console output
        print("\n" + "=" * 40)
        print("📤 ORDER REQUEST")
        print("-" * 40)
        print(f"Symbol      : {args.symbol}")
        print(f"Side        : {args.side}")
        print(f"Order Type  : {args.type}")
        print(f"Quantity    : {args.quantity}")
        if args.type == "LIMIT":
            print(f"Price       : {args.price}")
        print("=" * 40)

        logger.info(f"Order Request: {vars(args)}")

        # Submit order
        service = OrderService()
        response = service.submit(
            args.symbol, args.side, args.type, args.quantity, args.price
        )

        # Success output
        logger.info(f"Order Response: {response}")

        print("\n✅ ORDER PLACED SUCCESSFULLY")
        print("-" * 40)
        print("Order ID     :", response.get("orderId"))
        print("Status       :", response.get("status"))
        print("Executed Qty :", response.get("executedQty"))
        print("Avg Price    :", response.get("avgPrice", "N/A"))
        print("=" * 40)

    except Exception as e:
        print("\n❌ ORDER FAILED")
        print("-" * 40)
        print("Reason :", str(e))
        print("\n📄 Check logs for details")


if __name__ == "__main__":
    main()

