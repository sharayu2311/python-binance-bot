import time
import logging

class TWAPOrder:
    def __init__(self, client):
        self.client = client

    def execute(self, symbol, side, total_qty, chunks, delay_sec):
        """
        TWAP = Time-Weighted Average Price Strategy
        Splits a large order into smaller pieces executed over time.
        Example:
            total_qty = 0.02 BTC
            chunks = 4
            delay_sec = 10
            → Bot executes 4 orders of 0.005 BTC every 10 seconds.
        """

        logging.info(
            f"TWAP Start: symbol={symbol}, side={side}, total={total_qty}, "
            f"chunks={chunks}, interval={delay_sec}s"
        )

        qty_per_order = round(total_qty / chunks, 8)
        results = []

        for i in range(1, chunks + 1):
            print(f"\n📌 Executing TWAP order {i}/{chunks} → {qty_per_order} {symbol}")

            try:
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=qty_per_order
                )

                results.append(order)
                logging.info(f"TWAP success step {i}: {order}")
                print(f"✔️ Order executed.")

            except Exception as e:
                logging.error(f"TWAP error at step {i}: {e}")
                print(f"❌ Error while placing TWAP order: {e}")
                break  # stop execution on failure

            time.sleep(delay_sec)

        logging.info("TWAP Completed.")
        return results
