# filename : main.py

from order_book import OrderBook
from data_feed import get_mock_snapshot, get_mock_updates
from config import DISPLAY_LEVELS 

def print_book(book, levels = 10):
    print("\n" + "=" * 40)
    print("ORDER BOOK")
    print("=" * 40)
    
    print("\nASKS:")
    for price, size in reversed(book.get_top_asks(levels)):
        print(f"{price:>10.2f} | {size:>10.4f}")
        
    print("\n--- spread ---")
    print(f"Best Bid: {book.best_bid()}")
    print(f"Best Ask: {book.best_ask()}")
    
    print("\nBIDS:")
    for price, size in book.get_top_bids(levels):
        print(f"{price:>10.2f} | {size:>10.4f}")
        
def main():
    book = OrderBook()
    
    bids, asks = get_mock_snapshot()
    book.load_snapshot(bids, asks)
    
    print("Initial snapshot:")
    print_book(book, DISPLAY_LEVELS)
    
    updates = get_mock_updates()
    
    for i, (bid_updates, ask_updates) in enumerate(updates, start = 1):
        print(f"\nApplying update #{i}")
        book.apply_updates(bid_updates, ask_updates)
        print_book(book, DISPLAY_LEVELS)
        
if __name__ == "__main__":
    main()