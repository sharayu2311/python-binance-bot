import os
import logging
from dotenv import load_dotenv
from binance.client import Client


# ---------------- Logging Setup ---------------- #
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------- Helper Input Functions ---------------- #
def get_symbol_input() -> str:
    symbol = input("Enter trading pair (e.g., BTCUSDT, ETHUSDT): ").strip().upper()
    return symbol


def get_side_input() -> str:
    while True:
        side = input("Buy or Sell? (BUY/SELL): ").strip().upper()
        if side in ("BUY", "SELL"):
            return side
        print("⚠️ Invalid input. Please enter BUY or SELL.")


def get_float_input(prompt: str) -> float:
    while True:
        value = input(prompt).strip()
        try:
            value = float(value)
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("⚠️ Please enter a valid positive number.")


# ---------------- Core Bot Class ---------------- #
class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        """Initialize bot with Binance Futures Testnet API"""
        self.client = Client(api_key, api_secret, testnet=testnet)

        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logging.info("Bot initialized (Testnet Mode)")
        print("🔧 Bot initialized (Testnet Mode ON)")

    def place_market_order(self, symbol, side, quantity):
        """Place a market order"""
        logging.info(f"Attempting MARKET order → {symbol}, {side}, qty={quantity}")

        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
            logging.info(f"Market order success → {order}")
            print("\n✔️ Market Order Placed Successfully:\n", order)
            return order

        except Exception as e:
            logging.error(f"Market order error → {e}")
            print("\n❌ Error placing market order:", e)

    def place_limit_order(self, symbol, side, quantity, price):
        """Place a limit order"""
        logging.info(f"Attempting LIMIT order → {symbol}, {side}, qty={quantity}, price={price}")

        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=str(price)
            )
            logging.info(f"Limit order success → {order}")
            print("\n✔️ Limit Order Placed Successfully:\n", order)
            return order

        except Exception as e:
            logging.error(f"Limit order error → {e}")
            print("\n❌ Error placing limit order:", e)

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        """Place a Stop-Limit Order"""
        logging.info(
            f"Attempting STOP-LIMIT order → {symbol}, {side}, "
            f"qty={quantity}, stop={stop_price}, limit={limit_price}"
        )

        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="STOP",
                timeInForce="GTC",
                quantity=quantity,
                stopPrice=str(stop_price),
                price=str(limit_price)
            )
            logging.info(f"Stop-limit order success → {order}")
            print("\n✔️ Stop-Limit Order Placed Successfully:\n", order)
            return order

        except Exception as e:
            logging.error(f"Stop-limit order error → {e}")
            print("\n❌ Error placing stop-limit order:", e)

    def show_open_orders(self, symbol=None):
        """Optional: Show open orders for transparency"""
        try:
            if symbol:
                orders = self.client.futures_get_open_orders(symbol=symbol)
            else:
                orders = self.client.futures_get_open_orders()
            logging.info(f"Fetched open orders → {orders}")
            print("\n📌 Current Open Orders:")
            if not orders:
                print("No open orders.")
            else:
                for o in orders:
                    print(o)
        except Exception as e:
            logging.error(f"Error fetching open orders → {e}")
            print("\n❌ Error fetching open orders:", e)


# ---------------- Menu & Main Logic ---------------- #
def print_menu():
    print("\n=== 🧪 Binance Futures Testnet Trading Bot ===")
    print("1. Place MARKET order")
    print("2. Place LIMIT order")
    print("3. Place STOP-LIMIT order (Bonus)")
    print("4. View Open Orders")
    print("5. Exit")


def main():
    # Load environment variables
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("❌ Missing API keys. Make sure .env is configured.")
        return

    bot = BasicBot(api_key, api_secret)

    while True:
        print_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            # Market order
            symbol = get_symbol_input()
            side = get_side_input()
            quantity = get_float_input("Enter quantity: ")
            bot.place_market_order(symbol, side, quantity)

        elif choice == "2":
            # Limit order
            symbol = get_symbol_input()
            side = get_side_input()
            quantity = get_float_input("Enter quantity: ")
            price = get_float_input("Enter limit price: ")
            bot.place_limit_order(symbol, side, quantity, price)

        elif choice == "3":
            # Stop-limit order
            symbol = get_symbol_input()
            side = get_side_input()
            quantity = get_float_input("Enter quantity: ")
            stop_price = get_float_input("Enter stop (trigger) price: ")
            limit_price = get_float_input("Enter limit execution price: ")
            bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)

        elif choice == "4":
            # View open orders
            use_symbol_filter = input(
                "Filter by symbol? (y/n): "
            ).strip().lower()
            if use_symbol_filter == "y":
                symbol = get_symbol_input()
                bot.show_open_orders(symbol)
            else:
                bot.show_open_orders()

        elif choice == "5":
            print("👋 Exiting bot. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()
