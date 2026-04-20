# filename : data_feed_live.py

import json
import ssl
import websockets

from config import SYMBOL, WS_BASE_URL

async def partial_depth_stream(symbol=SYMBOL, levels=20, speed="100ms"):
    stream_name = f"{symbol.lower()}@depth{levels}@{speed}"
    url = f"{WS_BASE_URL}/{stream_name}"

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with websockets.connect(
        url,
        ping_interval=20,
        ping_timeout=60,
        ssl=ssl_context
    ) as ws:
        async for message in ws:
            yield json.loads(message)