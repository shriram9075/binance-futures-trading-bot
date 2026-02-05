def execute_order(client, logger, request: OrderRequest) -> dict:
    try:
        params = {
            "symbol": request.symbol,
            "side": request.side,
            "type": request.order_type,
            "quantity": request.quantity
        }

        if request.order_type == "LIMIT":
            params["price"] = request.price
            params["timeInForce"] = "GTC"

        # Log the request
        logger.info(f"Order Request: {params}")

        order = client.futures_create_order(**params)

        return {"success": True, "order": order}

    except Exception as e:
        logger.error(f"Order execution failed: {str(e)}")
        return {"success": False, "error": str(e)}
