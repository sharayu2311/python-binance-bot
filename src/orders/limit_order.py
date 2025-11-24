import logging

class LimitOrder:
    def __init__(self, client):
        self.client = client

    def place(self, symbol, side, quantity, price):
        logging.info(f"Limit order request: {symbol}, {side}, qty={quantity}, price={price}")
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=str(price)
            )
            logging.info(f"Limit order success: {order}")
            return order
        except Exception as e:
            logging.error(f"Limit order error: {e}")
            return {"error": str(e)}
