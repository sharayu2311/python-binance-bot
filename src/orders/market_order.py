from binance.client import Client
import logging

class MarketOrder:
    def __init__(self, client: Client):
        self.client = client

    def place(self, symbol, side, quantity):
        logging.info(f"Market order request: {symbol}, {side}, qty={quantity}")
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logging.info(f"Market order success: {order}")
            return order
        except Exception as e:
            logging.error(f"Market order error: {e}")
            return {"error": str(e)}
