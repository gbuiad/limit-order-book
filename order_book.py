# filename : order_book.py

class OrderBook:
    def __init__(self):
        self.bids = {}
        self.asks = {}
        self.last_update_id = None
    
    def load_snapshot(self, bids, asks, last_update_id=None):
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
                
        self.last_update_id = last_update_id
    
    def apply_updates(self, bid_updates, ask_updates, final_update_id=None):
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
                
        if final_update_id is not None:
            self.last_update_id = final_update_id
    
    def get_top_bids(self, n=10):
        return sorted(self.bids.items(), key=lambda x: -x[0])[:n]
    
    def get_top_asks(self, n=10):
        return sorted(self.asks.items(), key=lambda x: x[0])[:n]

    def best_bid(self):
        return max(self.bids.keys()) if self.bids else None 

    def best_ask(self):
        return min(self.asks.keys()) if self.asks else None 
    
    def mid_price(self):
        best_bid = self.best_bid()
        best_ask = self.best_ask()
        
        if best_bid is not None and best_ask is not None:
            return (best_bid + best_ask) / 2
        return None