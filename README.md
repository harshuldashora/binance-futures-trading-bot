# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based command-line trading bot that interacts with the Binance Futures Testnet (USDT-M). It allows users to place Market and Limit orders for both BUY and SELL sides while providing input validation, logging, and error handling.

## Features

* Place MARKET orders
* Place LIMIT orders
* Support for BUY and SELL order sides
* Command-line interface using argparse
* Input validation
* Structured project architecture
* Logging of API requests, responses, and errors
* Exception handling for invalid input, API errors, and network failures
* Binance Futures Testnet integration

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

## Requirements

* Python 3.10+
* Binance Futures Testnet Account
* Binance Testnet API Key and Secret

## Installation

Clone the repository:

```bash
git clone https://github.com/harshuldashora/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_api_secret
```

## Usage

### Place a Market Buy Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Market Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Place a Limit Buy Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### Place a Limit Sell Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Sample Output

### Market Order

```text
===== ORDER REQUEST =====
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001

===== ORDER RESPONSE =====
Order ID    : 13689700744
Status      : FILLED
ExecutedQty : 0.0010
Avg Price   : 72725.000000

SUCCESS: Order submitted successfully.
```

## Logging

All API requests, responses, and errors are stored in:

```text
logs/trading.log
```

Example:

```text
2026-06-01 21:15:03 | INFO | MARKET REQUEST | symbol=BTCUSDT side=BUY quantity=0.001
2026-06-01 21:15:04 | INFO | MARKET ORDER DETAILS | {'orderId':13689700744,'status':'FILLED'}
```

## Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Invalid quantity
* Invalid price
* Missing API credentials
* Binance API exceptions
* Network-related exceptions

## Assumptions

* User has a valid Binance Futures Testnet account.
* API credentials are configured correctly.
* Testnet account has sufficient virtual funds.
* Supported symbols are available on Binance Futures Testnet.

## Technologies Used

* Python 3
* python-binance
* python-dotenv
* argparse
* logging

## Author

Harshul Dashora
