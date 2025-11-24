import logging

class StopLimitOrder:
    def __init__(self, client):
        self.client = client

    def place(self, symbol, side, quantity, stop_price, limit_price):
        logging.info(
            f"Stop-limit request: {symbol}, {side}, qty={quantity}, stop={stop_price}, limit={limit_price}"
        )
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                timeInForce="GTC",
                quantity=quantity,
                stopPrice=str(stop_price),
                price=str(limit_price)
            )
            logging.info(f"Stop-limit order success: {order}")
            return order
        except Exception as e:
            logging.error(f"Stop-limit order error: {e}")
            return {"error": str(e)}
