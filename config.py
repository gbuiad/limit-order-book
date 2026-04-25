# SYMBOL : which asset simulated
SYMBOL = "BTCUSDT"

# SNAPSHOT_LIMIT : how many price levels loaded initially
SNAPSHOT_LIMIT = 20

# DISPLAY_LEVELS : how many levels printed
DISPLAY_LEVELS = 10

REST_DEPTH_URL = "https://data-api.binance.vision/api/v3/depth"

WS_BASE_URL = "wss://data-stream.binance.vision/ws"

# IMBALANCE SIGNAL CODE UPDATE
IMBALANCE_LEVELS = 5
BUY_THRESHOLD = 0.10
SELL_THRESHOLD = -0.10
MAX_SPREAD = 0.02

# PAPER TRADING SETTINGS : starting money, $/buy
INITIAL_CASH = 10000.0
TRADE_USD_SIZE = 1000.0
FEE_RATE = 0.001