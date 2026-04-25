# filname : paper_trader.py 

class PaperTrader:
    def __init__(self, initial_cash=10000.0, trade_usd_size=1000.0, fee_rate=0.001):
        self.initial_cash = initial_cash
        self.cash = initial_cash 
        self.trade_usd_size = trade_usd_size
        self.fee_rate = fee_rate
        
        self.position_btc = 0.0
        self.entry_price = None 
        
        self.realized_pnl = 0.0
        self.trade_count = 0
        self.last_action = "NONE"
    
    def has_position(self):
        return self.position_btc > 0
    
    def buy(self, ask_price):
        """
        Buy BTC using a fixed dollar amount at current best ask.
        """
        
        if ask_price is None:
            return "NO_BUY_NO_ASK"
        
        if self.has_position():
            return "ALREADY_LONG"
        
        usd_to_spend = min(self.trade_usd_size, self.cash)
        if usd_to_spend <= 0:
            return "NO_CASH"

        fee = usd_to_spend * self.fee_rate
        net_usd = usd_to_spend - fee
        
        btc_bought = net_usd / ask_price
        
        self.cash -= usd_to_spend
        self.position_btc = btc_bought
        self.entry_price = ask_price
        self.trade_count += 1
        self.last_action = f"BUY {btc_bought:.6f}"
        
        return self.last_action
    
    def sell(self, bid_price):
        """
        Sell all BTC at the current best bid.
        """
        if bid_price is None:
            return "NO_SELL_NO_BID"
        
        if not self.has_position():
            return "NO_POSITION"
        
        gross_usd = self.position_btc * bid_price
        fee = gross_usd * self.fee_rate 
        net_usd = gross_usd - fee 
        
        cost_basis = self.position_btc * self.entry_price 
        trade_pnl = net_usd - cost_basis
        
        self.cash += net_usd 
        self.realized_pnl += trade_pnl 
        
        sold_btc = self.position_btc
        
        self.position_btc = 0.0
        self.entry_price = None
        self.trade_count += 1
        self.last_action = f"SELL {sold_btc:.6f} BTC @ {bid_price:.2f} | PnL {trade_pnl:.2f}"
        
        return self.last_action
    
    def mark_to_market(self, mid_price):
        """
        Portfolio value = cash + current BTC position marked at mid price.
        """
        
        if mid_price is None:
            return self.cash
        return self.cash + self.position_btc * mid_price
    
    def unrealized_pnl(self, mid_price):
        if not self.has_position() or self.entry_price is None or mid_price is None:
            return 0.0
        return self.position_btc * (mid_price - self.entry_price)
    
    def summary(self, mid_price):
        return {
            "cash": self.cash,
            "position_btc": self.position_btc,
            "entry_price": self.entry_price,
            "realized_pnl": self.realized_pnl,
            "unrealized_pnl": self.unrealized_pnl(mid_price),
            "portfolio_value": self.mark_to_market(mid_price),
            "trade_count": self.trade_count,
            "last_action": self.last_action,
        }