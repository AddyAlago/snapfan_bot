import json
import requests
import os
import datetime
from config import CARD_DATA_URL, CARD_DATA_PATH

def download_card_data(force=False):
    """Download full Snap.fan card list (with pagination) and save it locally."""
    if not force and is_data_fresh():
        print("🔄 Card data is up to date.")
        return

    print("⬇️ Fetching full Snap.fan card list...")

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; SnapBot/1.0)"
    }

    all_cards = []
    url = CARD_DATA_URL

    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        page_cards = data.get("results", [])
        all_cards.extend(page_cards)

        print(f"📦 Fetched {len(page_cards)} cards from: {url}")
        url = data.get("next")  # follow pagination

    os.makedirs(os.path.dirname(CARD_DATA_PATH), exist_ok=True)
    with open(CARD_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(all_cards, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved {len(all_cards)} cards to {CARD_DATA_PATH}")

def is_data_fresh():
    """Check if the local card data is less than 24 hours old."""
    if not os.path.exists(CARD_DATA_PATH):
        return False
    modified = os.path.getmtime(CARD_DATA_PATH)
    age = (datetime.datetime.now() - datetime.datetime.fromtimestamp(modified)).total_seconds()
    return age < 86400  # 24 hours


def load_card_data():
    """Load card data into a lookup dictionary."""
    with open(CARD_DATA_PATH, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    card_lookup = {}
    for card in raw_data:
        name = card["name"].lower()
        card_lookup[name] = {
            "ability": card.get("description", "No description."),
            "slug": card["url"].strip("/"),  # use slug from URL
            "cost": card.get("cost", "?"),
            "power": card.get("power", "?"),
        }
    return card_lookup