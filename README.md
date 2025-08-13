# 🃏 Marvel Snap Reddit Bot

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![PRAW](https://img.shields.io/badge/PRAW-Reddit%20API-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> 🤖 A Reddit bot that monitors **r/MarvelSnap** for card mentions and automatically replies with real-time card data from [Snap.fan](https://snap.fan/).

---

## ✨ Features

- **Real-Time Monitoring** – Watches for new posts and comments mentioning Marvel Snap cards.
- **Accurate Card Matching** – Handles cards with similar names (e.g., *Bishop* vs *Kate Bishop*).
- **Rate Limit Aware** – Complies with Reddit API limits to avoid bans.
- **Multiple Matches** – Responds with info for all matched cards in a comment.
- **Modular Code** – Clean, maintainable Python code using PRAW for Reddit integration.

---

## 📸 Example Interaction

**User Post:**  
> Just pulled *Galactus* — is he still meta?  

**Bot Reply:**  
> **Galactus** – [View on Snap.fan](https://snap.fan/cards/galactus/)  
> Energy: 6 | Power: 5  
> On Reveal: If this is your only card here, destroy all other locations.

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/marvel-snap-reddit-bot.git
cd marvel-snap-reddit-bot
