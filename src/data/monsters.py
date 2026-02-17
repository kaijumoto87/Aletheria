

def add_monster(name, health_range, loot_table, exp_reward, mana_range=None):
    monster = {
        "name": name,
        "health_range": health_range,
        "loot_table": loot_table,
        "exp_reward": exp_reward,
    }
    if mana_range:
        monster["mana_range"] = mana_range
    MONSTERS.append(monster)

MONSTERS = [
    {
        "name": "Goblin",
        "health_range": (10, 15),
        "attack_range": (6, 8),
        "loot_table": ["small health potion", "shille", "rusty sword"],
        "exp_reward": 10,
    },
    {
        "name": "Wolf",
        "health_range": (12, 18),
        "attack_range": (5, 7),
        "loot_table": ["wolf pelt", "sharp fang", "shille"],
        "exp_reward": 12,
    },
    {
        "name": "Orc",
        "health_range": (15, 22),
        "attack_range": (7, 10),
        "loot_table": ["orcish axe", "shille", "small health potion"],
        "exp_reward": 15,
    },
    {
        "name": "Dark Elf",
        "health_range": (18, 25),
        "attack_range": (8, 12),
        "mana_range": (5, 10),
        "loot_table": ["elven bow", "magic crystal", "small mana potion"],
        "exp_reward": 20,
    },
    {
        "name": "Bloody Bear",
        "health_range": (20, 30),
        "attack_range": (10, 15),
        "loot_table": ["bear claw", "thick fur", "large health potion"],
        "exp_reward": 25,
    },
    {
        "name": "Skeleton Warrior",
        "health_range": (15, 20),
        "attack_range": (6, 9),
        "loot_table": ["bone sword", "shield fragment", "shille"],
        "exp_reward": 18,
    },
    {
        "name": "Fenrir Wolf",
        "health_range": (40, 65),
        "attack_range": (15, 25),
         "mana_range": (10, 20),
        "loot_table": ["fenrir fang", "mythical pelt", "large health potion"],
        "exp_reward": 80,
    },
]