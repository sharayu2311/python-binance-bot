```markdown
# Binance Futures Testnet Trading Bot

A small, easy-to-read Python trading bot that demonstrates how to place Market, Limit and Stop-Limit orders on the Binance Futures Testnet from the command line. This project focuses on clear structure, input validation, logging, and safe testnet usage — ideal for learning the basics of programmatic trading without risking real funds.

---

## Table of contents

- [Key features](#key-features)
- [Tech stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [Logging](#logging)
- [Notes & limitations](#notes--limitations)
- [Suggested improvements](#suggested-improvements)
- [Contributing](#contributing)
- [License & author](#license--author)

---

## Key features

- Place Market, Limit and Stop-Limit orders (Buy / Sell) on Binance Futures **Testnet**
- Interactive, menu-driven command-line interface
- Input validation and simple error handling
- Logging of requests, responses and errors (bot.log)
- View open orders

---

## Tech stack

- Python 3.x
- python-binance (for API communication)
- python-dotenv (for environment variables / credentials)

---

## Prerequisites

- Python 3.8+
- A Binance Futures Testnet account and API key:
  - Testnet URL: https://testnet.binancefuture.com
  - Create API key under: API Management → Create API Key
  - Enable Trading and Futures permissions for the test API key

---

## Quick start

1. Clone the repository:
   ```bash
   git clone https://github.com/sharayu2311/python-binance-bot.git
   cd python-binance-bot
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS / Linux
   # or
   venv\Scripts\activate      # Windows (PowerShell/CMD)
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If the repository doesn't include requirements.txt:
   ```bash
   pip install python-binance python-dotenv
   ```

---

## Configuration

Create a `.env` file in the project root and add your Testnet API credentials:

```
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
```

Important: Do NOT use live API keys with this project unless you intentionally want to trade on the live platform. This bot is written for the Testnet environment only.

---

## Usage

Run the bot:

```bash
python3 basic_bot.py
```

When started you will see a menu like:

1. Place Market Order  
2. Place Limit Order  
3. Place Stop-Limit Order  
4. View Open Orders  
5. Exit

Follow the prompts to enter:
- Trading symbol (e.g., BTCUSDT, ETHUSDT)
- Order side (BUY or SELL)
- Quantity
- Price (for Limit / Stop-Limit)

All placed orders and key actions are written to `bot.log` for auditing and debugging.

Example session snippet:
```
Select an option: 1
Enter symbol: BTCUSDT
Side (BUY/SELL): BUY
Quantity: 0.001
Order placed: Market BUY 0.001 BTCUSDT
```

---

## Logging

- The bot logs requests, responses and errors to `bot.log` in the project directory.
- Use the log to verify what was sent to the API and to debug failures.

---

## Notes & limitations

- This project is for learning and demonstration only.
- It only works with the Binance Futures Testnet (not live trading).
- Binance minimum order value rules still apply (orders below the exchange's minimum notional may be rejected).
- The bot does not implement:
  - Position management / risk controls
  - Order lifecycle handling beyond placing and listing open orders
  - Any automated trading strategies or indicators

---

## Suggested improvements (next steps)

- Add configuration for switching between Testnet and Live (with clear safety checks)
- Support OCO (One Cancels Other) and Grid orders
- Show account balance and position information
- Add unit tests and integration tests (with recorded responses / mocking)
- Build a lightweight GUI or web interface for easier interaction
- Implement retry/backoff and more robust error handling for API rate limits

---

## Contributing

Contributions, issues and suggestions are welcome. If you add features, please:
- Open a descriptive issue first
- Send a pull request with tests and documentation updates

---

## License & author

Author: Sharayu Bodkhe  
Created as part of the TradeScan internship application project.

```
