# filename : main_live.py

import asyncio

from order_book import OrderBook
from data_feed_live import partial_depth_stream
from config import DISPLAY_LEVELS, SYMBOL

def print_book(book, levels=10):
    print("\033[2J\033[H", end="")
    print("=" * 50)
    print(f"LEVEL 2 ORDER BOOK: {SYMBOL}")
    print("=" * 50)

    print("\nASKS:")
    asks = book.get_top_asks(levels)
    for price, size in reversed(asks):
        print(f"{price:>12.2f} | {size:>12.6f}")

    print("\n--- market ---")
    print(f"Best Bid: {book.best_bid()}")
    print(f"Best Ask: {book.best_ask()}")
    print(f"Mid     : {book.mid_price()}")

    print("\nBIDS:")
    bids = book.get_top_bids(levels)
    for price, size in bids:
        print(f"{price:>12.2f} | {size:>12.6f}")

async def main():
    book = OrderBook()

    async for event in partial_depth_stream(levels=20, speed="100ms"):
        bids = event.get("bids", [])
        asks = event.get("asks", [])

        book.load_snapshot(bids, asks)
        print_book(book, DISPLAY_LEVELS)

if __name__ == "__main__":
    asyncio.run(main())