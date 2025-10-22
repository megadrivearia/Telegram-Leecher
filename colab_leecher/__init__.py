# copyright 2023 © Xron Trix | https://github.com/Xrontrix10
import logging, json
import asyncio
import sys

# --- FIX: force creation of an event loop for Python 3.12 ---
if sys.version_info >= (3, 12):
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

# --- disable uvloop completely (Colab doesn't need it) ---
try:
    import uvloop
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
except Exception as e:
    print("⚠️ uvloop not available or disabled:", e)
from pyrogram.client import Client

# Read the dictionary from the txt file
with open("/content/Telegram-Leecher/credentials.json", "r") as file:
    credentials = json.loads(file.read())

API_ID = credentials["API_ID"]
API_HASH = credentials["API_HASH"]
BOT_TOKEN = credentials["BOT_TOKEN"]
OWNER = credentials["USER_ID"]
DUMP_ID = credentials["DUMP_ID"]


logging.basicConfig(level=logging.INFO)

install()

colab_bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
