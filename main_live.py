# filename : main_live.py

# creates a fixed screen
# redrawns the same tables
# updates values in place
# keep best bid and ask at the top

import asyncio

from rich.live import Live
from rich.table import Table 
from rich.console import Group 
from rich.panel import Panel 

from order_book import OrderBook
from data_feed_live import partial_depth_stream
from config import DISPLAY_LEVELS, SYMBOL
from signals import get_signal

def build_display(book, levels = 10):
    best_bid = book.best_bid()
    best_ask = book.best_ask()
    mid = book.mid_price()
    
    sgnl, imbalance, spread = get_signal(book)
        
    summary = Table.grid(padding = 1)
    summary.add_row("Symbol: ", SYMBOL)
    summary.add_row("Best Bid: ", f"{best_bid:.2f}" if best_bid is not None else "None")
    summary.add_row("Best Ask: ", f"{best_ask:.2f}" if best_ask is not None else "None")
    summary.add_row("Spread: ", f"{spread:.2f}" if spread is not None else "None")
    summary.add_row("Mid: ", f"{mid:.2f}" if mid is not None else "None")
    summary.add_row("Imbalance: ", f"{imbalance:.3f}")
    summary.add_row("Signal: ", sgnl)
    
    ask_table = Table(title = "ASKS")
    ask_table.add_column("Price", justify = "right")
    ask_table.add_column("Size", justify = "right")
    
    asks = book.get_top_asks(levels)
    for price, size in reversed(asks):
        ask_table.add_row(f"{price:.2f}", f"{size:.2f}")
    
    bid_table = Table(title = "BIDS")
    bid_table.add_column("Price", justify = "right")
    bid_table.add_column("Size", justify = "right")
    
    bids = book.get_top_bids(levels)
    for price, size in bids:
        bid_table.add_row(f"{price:.2f}", f"{size:.2f}")
        
    return Group(
        Panel(summary, title = "Market Summary"),
        ask_table,
        bid_table
    )
    
async def main():
    book = OrderBook()

    with Live(build_display(book, DISPLAY_LEVELS), refresh_per_second = 4, screen = False) as live:
        async for event in partial_depth_stream(levels = 20, speed = '100ms'):
            bids = event.get("bids", [])
            asks = event.get("asks", [])
            
            book.load_snapshot(bids, asks)
            live.update(build_display(book, DISPLAY_LEVELS))

if __name__ == "__main__":
    asyncio.run(main())