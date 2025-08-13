import praw
import time
import re
from config import *
from card_data import download_card_data, load_card_data
from responder import find_cards_in_text, format_reply
from praw.exceptions import APIException

# Download latest card data
download_card_data()

# Load card data into memory
card_lookup = load_card_data()

# Connect to Reddit
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=USER_AGENT
)

subreddit = reddit.subreddit("testsnapbot")
print("🤖 Bot is live and monitoring r/MarvelSnap...")

for comment in subreddit.stream.comments(skip_existing=True):
    # Prevent replying to itself
    if comment.author == reddit.user.me():
        continue

    print(f"🔍 Checking comment {comment.id}: {comment.body}")

    matches = find_cards_in_text(comment.body.lower(), card_lookup)
    print(f"🔗 Matches found: {matches}")

    if matches:
        reply_parts = []
        for match in matches:
            reply_parts.append(format_reply(match, card_lookup[match]))
        reply = "\n\n---\n\n".join(reply_parts)

        try:
            comment.reply(reply)
            print(f"✅ Replied to {comment.id} about: {', '.join(matches)}")
        except APIException as e:
            if e.error_type == "RATELIMIT":
                delay_search = re.search(r"(\d+)\s+(minute|second)", e.message)
                if delay_search:
                    delay_amount = int(delay_search.group(1))
                    delay_unit = delay_search.group(2)
                    delay_seconds = delay_amount * 60 if "minute" in delay_unit else delay_amount

                    print(f"⏳ Rate limited. Sleeping for {delay_seconds} seconds...")
                    time.sleep(delay_seconds + 5)  # buffer

                    try:
                        comment.reply(reply)
                        print(f"✅ Retried and replied to {comment.id}")
                    except Exception as retry_error:
                        print(f"❌ Retry failed: {retry_error}")
                else:
                    print("⚠️ Rate limit detected but could not parse delay.")
            else:
                print(f"❌ APIException: {e}")
        except Exception as e:
            print(f"❌ Failed to reply to {comment.id}: {e}")
