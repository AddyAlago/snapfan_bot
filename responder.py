
import re


def find_cards_in_text(text, card_lookup):
    """Return a list of all card names mentioned in the text."""
    matches = []
    for card_name in card_lookup:
        pattern = r"\b" + re.escape(card_name) + r"\b"
        if re.search(pattern, text, flags=re.IGNORECASE):
            matches.append(card_name)
    return matches


def format_reply(card_name, card_info):
    """Create a nicely formatted Reddit reply for a card."""
    slug = card_info['slug'].strip("/")
    link = f"https://snap.fan/{slug}"
    raw_ability = card_info.get("ability", "No description.")

    # Preserve <b> tags as Markdown bold (**), remove everything else
    ability = raw_ability.replace("<b>", "**").replace("</b>", "**")
    ability = re.sub(r"<.*?>", "", ability).strip()

    cost = card_info.get("cost", "?")
    power = card_info.get("power", "?")

    return (
        f"**[{card_name.title()}]({link})**  \n"
        f"**🟦 {cost}-Cost**, **🟥 {power}-Power**  \n"
        f"> {ability}"
    )
