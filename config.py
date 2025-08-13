from dotenv import load_dotenv
import os

load_dotenv()  # ✅ Loads variables from .env into environment

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
USER_AGENT = "SnapFanBot/0.1 by u/YourUsername"

CARD_DATA_PATH = "snapfan_bot/data/snapfan_cards.json"
CARD_DATA_URL = "https://snap.fan/api/cards/"