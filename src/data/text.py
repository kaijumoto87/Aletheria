# In-game text and dialogues in Japanese and English for Aletheria game.

def get_text(key: str, lang: str = "en") -> str:
    if key not in TEXT:
        return ""
    if lang not in LANGUAGES:
        lang = "en"
    return TEXT[key].get(lang, "")

LANGUAGES = ("en", "jp")

TEXT = {
    "game.start": {
        "en": "Your adventure begins...",
        "jp": "ぼうけんがはじまる...",
    },
    "combat.attack": {
        "en": "You strike the {monster} for {damage} damage!",
        "jp": "{monster}に{damage}のダメージを与えた！",
    },
}