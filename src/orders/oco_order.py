import logging

class OCOOrder:
    def __init__(self, client):
        self.client = client

    def place(self, symbol, side, quantity, take_profit_price, stop_price, stop_limit_price):
        """
        OCO = Take Profit Limit + Stop-Loss Limit
        stop_price → trigger for stop loss
        stop_limit_price → execution price after stop loss triggers
        """

        logging.info(
            f"OCO order → {symbol}, {side}, qty={quantity}, TP={take_profit_price}, "
            f"STOP={stop_price}, STOP-LIMIT={stop_limit_price}"
        )

        try:
            response = self.client.futures_place_order(
                symbol=symbol,
                side=side,
                type="OCO",
                quantity=quantity,
                price=str(take_profit_price),  # take profit limit price
                stopPrice=str(stop_price),      # trigger price
                stopLimitPrice=str(stop_limit_price),
                stopLimitTimeInForce="GTC"
            )

            logging.info(f"OCO success → {response}")
            return response

        except Exception as e:
            logging.error(f"OCO order error → {e}")
            return {"error": str(e)}
