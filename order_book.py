# filename : order_book.py

class OrderBook:
    def __init__(self):
        self.bids = {}
        self.asks = {}
    
    def load_snapshot(self, bids, asks):
        self.bids = {}
        self.asks = {}
        
        for price, size in bids:
            price = float(price)
            size = float(size)
            
            if size > 0:
                self.bids[price] = size
        
        for price, size in asks:
            price = float(price)
            size = float(size)
            
            if size > 0:
                self.asks[price] = size
    
    def apply_updates(self, bid_updates, ask_updates):
        for price, size in bid_updates:
            price = float(price)
            size = float(size)
            
            if size == 0:
                self.bids.pop(price, None)
            else:
                self.bids[price] = size
        
        for price, size in ask_updates:
            price = float(price)
            size = float(size)
            
            if size == 0:
                self.asks.pop(price, None)
            else:
                self.asks[price] = size
    
    def get_top_bids(self, n = 10):
        return sorted(self.bids.items(), key = lambda x: -x[0])[:n]
    
    def get_top_asks(self, n = 10):
        return sorted(self.asks.items(), key = lambda x: x[0])[:n]

    def best_bid(self):
        return max(self.bids.keys()) if self.bids else None 

    def best_ask(self):
        return min(self.asks.keys()) if self.asks else None 