import json
from pathlib import Path
from datetime import datetime

SAVE_VERSION = 1

SAVE_DIR = Path(__file__).resolve().parents[1] / "saves"
SAVE_PATH = SAVE_DIR / "save.json"


def save_player(player: dict, path: Path = SAVE_PATH) -> None:
    SAVE_DIR.mkdir(parents=True, exist_ok=True)

    data = {
        "version": SAVE_VERSION,
        "saved_at": datetime.now().isoformat(timespec="seconds"),
        "player": {
            # core
            "name": player.get("name", ""),
            "level": player.get("level", 1),
            "exp": player.get("exp", 0),
            "exp_to_next": player.get("exp_to_next", 10),

            # stats
            "health": player.get("health", 20),
            "strength": player.get("strength", 5),
            "courage": player.get("courage", 20),
            "mana": player.get("mana", 10),

            # inventory
            "inventory": list(player.get("inventory", [])),

            # extras
            "equipped_weapon": player.get("equipped_weapon", "fists"),
            "weapon_bonus": player.get("weapon_bonus", 0),
            "coins": player.get("coins", 0),
        },
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_player(path: Path = SAVE_PATH) -> dict | None:
    if not path.exists():
        return None

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("Save file is corrupted.")
        return None

    if data.get("version") != SAVE_VERSION:
        print(f"Unsupported save version: {data.get('version')}")
        return None

    p = data.get("player", {})

    # defaults so old saves won’t break when you add new fields later
    return {
        "name": p.get("name", ""),
        "level": p.get("level", 1),
        "exp": p.get("exp", 0),
        "exp_to_next": p.get("exp_to_next", 10),
        "health": p.get("health", 20),
        "strength": p.get("strength", 5),
        "courage": p.get("courage", 20),
        "mana": p.get("mana", 10),
        "inventory": [str(x).strip().lower() for x in p.get("inventory", [])],
        "equipped_weapon": str(p.get("equipped_weapon", "fists")).strip().lower(),
        "weapon_bonus": int(p.get("weapon_bonus", 0)),
        "coins": int(p.get("coins", 0)),
    }