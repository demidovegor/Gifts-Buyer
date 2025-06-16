import urllib.request
from app.utils.logger import error
from data.config import config

async def send_heartbeat():
    try:
        urllib.request.urlopen(config.HEARTBEAT_MONITOR_URL, timeout=2)
    except Exception as e:
        error(f"Heartbeat failed: {e}")
