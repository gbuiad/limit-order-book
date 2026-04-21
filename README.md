# Limit Order Book Simulator
# Author: gbuiad

This project implements a Level 2 limit order book in Python.

## Features
- Maintains bid/ask price levels
- Supports dynamic updates (add/remove levels)
- Tracks best bid/ask and spread
- Simulates real-time order book updates using mock data

## Structure
- `order_book.py`: core data structure
- `data_feed.py`: mock market data
- `main.py`: simulation runner
- `config.py`: settings

## Future Work
- integrate real-time market data (Binance)
- compute order imbalance
- build trading strategies on top

## Modes

### Mock Mode
Runs a simulated order book with predefined updates.

```bash
python3 main_mock.py