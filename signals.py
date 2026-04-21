# filename : signals.py 
# IMBALANCE SIGNAL CODE UPDATE

from config import IMBALANCE_LEVELS, BUY_THRESHOLD, MAX_SPREAD, SELL_THRESHOLD

def compute_imbalance(book, levels = IMBALANCE_LEVELS):
    bids = book.get_top_bids(levels)
    asks = book.get_top_asks(levels)
    
    bid_size = sum(size for _, size in bids)
    ask_size = sum(size for _, size in asks)
    
    total = bid_size + ask_size
    if total == 0:
        return 0.0
    
    return (bid_size - ask_size) / total 

def get_signal(book):
    best_bid = book.best_bid()
    best_ask = book.best_ask()
    
    if best_bid is None or best_ask is None:
        return "HOLD", 0.0, None
    
    spread = best_ask - best_bid
    imbalance = compute_imbalance(book)
    
    if spread <= MAX_SPREAD:
        if imbalance >= BUY_THRESHOLD:
            return "BUY", imbalance, spread 
        elif imbalance <= SELL_THRESHOLD:
            return "SELL", imbalance, spread
        
    return "HOLD", imbalance, spread