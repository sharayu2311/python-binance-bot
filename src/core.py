import os
import logging
from dotenv import load_dotenv
from binance.client import Client

# Order imports
from orders.market_order import MarketOrder
from orders.limit_order import LimitOrder
from orders.stop_limit_order import StopLimitOrder
from orders.oco_order import OCOOrder
from advanced.twap_order import TWAPOrder
from advanced.grid_order import GridOrder


# ---------------- Logging Setup ---------------- #
logging.basicConfig(
    filename="../bot.log",  # save outside src
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------- Helper Input Functions ---------------- #
def get_symbol() -> str:
    return input("Enter trading pair (e.g., BTCUSDT, ETHUSDT): ").strip().upper()


def get_side() -> str:
    while True:
        value = input("Order side (BUY/SELL): ").strip().upper()
        if value in ("BUY", "SELL"):
            return value
        print("Invalid input. Enter only BUY or SELL.")


def get_float(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt))
            if val > 0:
                return val
        except:
            pass
        print("Invalid number, try again.")


# ---------------- Bot Class ---------------- #
class BinanceBot:
    def __init__(self, key, secret):
        self.client = Client(key, secret, testnet=True)

        # Required Binance Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Modules
        self.market = MarketOrder(self.client)
        self.limit = LimitOrder(self.client)
        self.stop_limit = StopLimitOrder(self.client)
        self.oco = OCOOrder(self.client)
        self.twap = TWAPOrder(self.client)
        self.grid = GridOrder(self.client)

        logging.info("Bot initialized")
        print("\nConnected to Binance Futures Testnet.\n")


    def show_open_orders(self, symbol=None):
        """Display open futures orders."""
        try:
            orders = (
                self.client.futures_get_open_orders(symbol=symbol)
                if symbol else
                self.client.futures_get_open_orders()
            )

            print("\n--- OPEN ORDERS ---\n")
            if orders:
                for o in orders:
                    print(o)
            else:
                print("No open orders.")

        except Exception as e:
            print("Error retrieving orders:", e)
            logging.error(f"Open orders fetch error → {e}")


# ---------------- Menu ---------------- #
def print_menu():
    print("\n===== Binance Trading Bot Menu =====")
    print("1. Place MARKET Order")
    print("2. Place LIMIT Order")
    print("3. Place STOP-LIMIT Order")
    print("4. Place OCO Order (Take Profit + Stop Loss)")
    print("5. Run TWAP Strategy")
    print("6. Run GRID Strategy")
    print("7. View Open Orders")
    print("8. Exit")


# ---------------- Main Loop ---------------- #
def run():
    load_dotenv()

    key = os.getenv("BINANCE_API_KEY")
    secret = os.getenv("BINANCE_API_SECRET")

    if not key or not secret:
        print("❌ Missing API keys in .env")
        return

    bot = BinanceBot(key, secret)

    while True:
        print_menu()
        choice = input("\nSelect an option (1-8): ").strip()

        if choice == "1":
            result = bot.market.place(
                get_symbol(),
                get_side(),
                get_float("Quantity: ")
            )
            print("\nResponse:", result)

        elif choice == "2":
            result = bot.limit.place(
                get_symbol(),
                get_side(),
                get_float("Quantity: "),
                get_float("Limit Price: ")
            )
            print("\nResponse:", result)

        elif choice == "3":
            result = bot.stop_limit.place(
                get_symbol(),
                get_side(),
                get_float("Quantity: "),
                get_float("Stop Trigger Price: "),
                get_float("Stop-Limit Execution Price: ")
            )
            print("\nResponse:", result)

        elif choice == "4":
            result = bot.oco.place(
                get_symbol(),
                get_side(),
                get_float("Quantity: "),
                get_float("Take Profit Price: "),
                get_float("Stop Price (Trigger): "),
                get_float("Stop-Limit Execution Price: ")
            )
            print("\nResponse:", result)

        elif choice == "5":
            symbol = get_symbol()
            side = get_side()
            total_qty = get_float("Total Quantity for TWAP: ")
            chunks = int(get_float("Number of chunks: "))
            delay = get_float("Delay between orders (seconds): ")

            print("\nRunning TWAP Strategy...")
            result = bot.twap.execute(symbol, side, total_qty, chunks, delay)
            print("\nTWAP Result:", result)

        elif choice == "6":
            symbol = get_symbol()
            side = get_side()
            qty = get_float("Order quantity per grid level: ")
            start = get_float("Grid start price: ")
            end = get_float("Grid end price: ")
            levels = int(get_float("Number of grid levels: "))

            print("\nRunning GRID Strategy...")
            result = bot.grid.execute(symbol, side, qty, start, end, levels)
            print("\nGRID Result:", result)

        elif choice == "7":
            filter_symbol = input("Filter by symbol? (y/n): ").strip().lower()
            bot.show_open_orders(get_symbol() if filter_symbol == "y" else None)

        elif choice == "8":
            print("\nExiting bot... Goodbye.")
            break

        else:
            print("Invalid option. Enter 1–8.")


if __name__ == "__main__":
    run()
