import logging


def validate_order(args):
    if args.side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if args.type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if args.quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if args.type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")
