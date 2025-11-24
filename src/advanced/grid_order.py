import logging

class GridOrder:
    def __init__(self, client):
        self.client = client

    def execute(self, symbol, side, qty, start_price, end_price, levels):
        """
        Simple GRID Trading Strategy:
        - Places multiple LIMIT orders between start_price and end_price.
        - If BUY → places buy orders spaced downward.
        - If SELL → places sell orders spaced upward.
        """

        if levels < 2:
            return {"error": "Grid levels must be at least 2"}

        logging.info(
            f"GRID Strategy Start → {symbol}, {side}, qty={qty}, range=({start_price} → {end_price}), levels={levels}"
        )

        # Determine price spacing
        step = (end_price - start_price) / (levels - 1)

        responses = []

        print("\nExecuting GRID Strategy...\n")

        for i in range(levels):
            price = round(start_price + (step * i), 2)

            logging.info(f"GRID Order {i+1}/{levels} at price={price}")

            try:
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    timeInForce="GTC",
                    quantity=qty,
                    price=str(price)
                )
                responses.append(order)
                print(f"✔️ Placed GRID order {i+1}/{levels} at {price}")
            except Exception as e:
                error_msg = f"❌ Failed placing GRID order {i+1}: {e}"
                print(error_msg)
                logging.error(error_msg)

        logging.info("GRID Strategy Completed")
        print("\nGRID Strategy Execution Completed.")
        return responses
