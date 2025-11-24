Binance Futures Testnet Trading Bot

This project is a Python-based trading bot built specifically for the Binance Futures Testnet.
It allows users to place Market, Limit, and Stop-Limit orders directly from the command line.
The goal of the project was to create a simplified trading workflow with proper structure, logging, error handling, and clean user interaction.

1. Project Purpose

The bot demonstrates:

Integration with the Binance Testnet API

Automating basic trading operations

Input validation and structured command flow

Practical logging for debugging and auditing

Safe testing environment (no real funds involved)

2. Features Included

Market order execution (Buy/Sell)

Limit order execution (Buy/Sell)

Stop-Limit order support (Bonus requirement)

Interactive menu-based command-line interface

Order validation and user input sanitization

Logging of requests, responses, and errors

Ability to view all open orders

3. Technologies Used

Python 3

python-binance (for API communication)

dotenv (to securely manage API credentials)

4. How to Set Up

Clone or download the repository.

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install python-binance python-dotenv


Create a .env file in the project folder and add your Binance Testnet API credentials:

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here


To generate these credentials, log in to:
https://testnet.binancefuture.com
 → API Management → Create API Key
Enable Trading and Futures permissions.

5. How to Use the Bot

Run the bot using:

python3 basic_bot.py


You will see a menu with options such as:

1. Place Market Order
2. Place Limit Order
3. Place Stop-Limit Order
4. View Open Orders
5. Exit


Follow the prompts to input:

Trading symbol (e.g., BTCUSDT, ETHUSDT)

Order side (BUY or SELL)

Quantity

Price values (where applicable)

All placed orders are logged in bot.log for reference.

6. Notes and Limitations

This bot is made for learning and demonstration only.

It works only with Binance Futures Testnet, not the live trading platform.

Minimum order value rules still apply (for example, Binance may reject orders under ~$100 notional value).

The bot does not include automated trading strategies, indicators, or position management—only order execution.

7. Future Improvements (Possible Extensions)

Add OCO or Grid order support

Build a lightweight GUI or web interface

Add balance display and order status polling

Integrate basic strategy (moving average, breakout, etc.)

8. Author

Sharayu Bodkhe
Created as part of the TradeScan internship application project.