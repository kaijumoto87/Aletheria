print("Welcome to Aletheria!")
print("You have now entered a world of magic and lies...")
print("Seek the truth, adventurer. Survive if you can...")
print()
print()

name = input("What is your name adventurer? ")
print(f"Welcome, {name}!")
print()

# PLAYER STATS
import random

def create_player() -> dict:
    """Create and return a new player state dict."""
    return {
        "level": 1,
        "exp": 0,
        "exp_to_next": 10,
        "health": random.randint(18, 24),
        "strength": random.randint(4, 7),
        "courage": random.randint(20, 35),
        "mana": random.randint(10, 15),
        "inventory": [],
        "equipped_weapon": "Fists",
        "weapon_bonus": 0,
    }

def show_player_stats(p: dict) -> None:
    print("\nYour stats:")
    print(f"Level: {p['level']}")
    print(f"Health: {p['health']}")
    print(f"Strength: {p['strength']}")
    print(f"Courage: {p['courage']}")
    print(f"Mana: {p['mana']}\n")


def get_crit_chance(courage):
      """
      Turn courage into a critical-hit chance.
      Returns a number between 0.0 and 0.20 (0%-20%).
      """
      base = 0.001 # 0.1 at courage 1
      # choose a slope so that around courage 35 you reach ~20%
      scale = (0.20 - base) / 34

      chance = base + scale * (courage - 1)

      # clamp between 0 and 20%
      if chance < 0:
            chance = 0
      if chance > 0.20:
            chance = 0.20
      
      return chance

level = 1
exp = 0
exp_to_next = 10

weapon_stats = {
    "fists": 0,
    "Bronze dagger": 3,
    "Rusty sword": 5,
    "Orcish axe": 8,
    "Elven bow": 6,
}

"""
Monster types: name, health range, loot table, exp reward:
Expand into more types
Make section for region based monsters...
"""
MONSTERS = [
      {
            "name": "Goblin",
            "health_range": (10, 15),
            "loot_table": ["Small health potion", "Gold coin", "Rusty sword"],
            "exp_reward": 10,
      },
      {
            "name": "Wolf",
            "health_range": (12, 18),
            "loot_table": ["Wolf pelt", "Sharp fang", "Gold coin"],
            "exp_reward": 12,
      },
      {
            "name": "Orc",
            "health_range": (15, 22),
            "loot_table": ["Orcish axe", "Gold coin", "Health potion"],
            "exp_reward": 15,
      },
      {
            "name": "Dark Elf",
            "health_range": (18, 25),
            "mana_range": (5,10),
            "loot_table": ["Elven bow", "Magic crystal", "Mana potion"],
            "exp_reward": 20,
      },
      {
            "name": "Bloody Bear",
            "health_range": (20, 30),
            "loot_table": ["Bear claw", "Thick fur", "Large health potion"],
            "exp_reward": 25,
      },
      {
            "name": "Skeleton Warrior",
            "health_range": (15, 20),
            "loot_table": ["Bone sword", "Shield fragment", "Gold coin"],
            "exp_reward": 18,
      },
      {
            "name": "Fenrir Wolf",
            "health_range": (40, 65),
            "loot_table": ["Fenrir fang", "Mythical pelt", "Large health potion"],
            "exp_reward": 80,
      }
      ]

"""
Add more monster types, each with their own stats and loot tables.
Add player stats block so don't need to rewrite each time.
Rewrite combat to be a function...
"""

player = create_player()

print(f"Your starting stats:")
show_player_stats(player)

print()  # blank line for spacing

choice = input("Do you want to enter the Dark Forest? (yes/no) ").lower()

if choice == "yes":
    print("You step into the forest. The trees seem to whisper your name...")

    # SECOND CHOICE
    print()
    forest_choice = input("You see a strange glow on the path. Do you follow it or ignore it? (follow/ignore) ").lower()

    if forest_choice == "follow":
            print("You follow a small chest pulsing with light.")
            print("You open it and find a bronze dagger inside!")
            player['inventory'].append("Bronze dagger")
            player['equipped_weapon'] = "Bronze dagger"
            player['weapon_bonus'] = 3

            print("You equip the Bronze dagger")
            print(f"Weapon bonus: +{player['weapon_bonus']} attack")
            print("You can type 'equip' later to change weapons.")
            print()
            print("Armed with your new weapon, you return to the main path.")
    
    elif forest_choice == "ignore":
            print("You stay on the main path, feeling a chill, but staying safe... for now.")
    else:
            print("You hesitate too long, the glow fades into the darkness.")
    print("You continue along the path...")
    print()
    
    investigate_choice = input("You hear a rustling noise in the bushes nearby! Do you run away or investigate? (run/investigate) ").lower()

    if investigate_choice == "investigate":
          encounter_chance = random.randint(1,100)

          if encounter_chance <= 100: # 100% chance for testing
                print("A monster leaps out from the shadows!")

                monster_health = random.randint(10,18)
                print(f"Monster Health: {monster_health}")

                escaped = False #track if successfully ran away

                while monster_health > 0 and player['health'] > 0: 
                        print()
                        action = input("Do you want to attack or run? (Choose: attack, run, inv, stats, equip): ").lower()

                        if action == "inv":
                              print("\nYour Inventory:")
                              if player['inventory']:
                                    for item in player['inventory']:
                                          print(f"- {item}")
                              else:
                                    print("(Empty)")
                              print()
                              continue
                        elif action == "stats":
                              show_player_stats(player)
                              print(f"Strength: {player['strength']}")
                              print(f"Courage: {player['courage']}\n")
                              continue
                        elif action == "attack":
                            # 1 figure out crit chance from courage
                            crit_chance = get_crit_chance(player['courage'])

                            # 2 roll for normal damage
                            player_damage = random.randint(1,player['strength'] + player['weapon_bonus'])

                            # 3 roll to see if it crits
                            if random.random() < crit_chance:
                                  player_damage *= 2
                                  print("Critical hit! Your attack deals double damage!")
                            
                            # monster's turn
                            monster_damage = random.randint(1,6)

                            monster_health -= player_damage
                            player['health'] -= monster_damage

                            print(f"You hit the monster for {player_damage} damage!")
                            print(f"The monster hit you for {monster_damage} damage!")
                            print(f"Your health: {player['health']}")
                            print(f"Monster health: {monster_health}")

                        elif action == "run":
                            #Try to roll to escape - roll between 1 and 100
                            escape_roll = random.randint(1,100)
                            if escape_roll <= 60:
                                  print("\nYou turn and flee! You manage to escape the monster!")
                                  player['courage'] -= 1
                                  print(f"courage: {player['courage']}")
                                  escaped = True
                                  break
                            else:
                                  print("\nYou try to run, but the monster blocks your path!")
                                  monster_damage = random.randint(1,6)
                                  player['health'] -= monster_damage
                                  print(f"The monster strikes you for {monster_damage} damage as you flee!")
                                  print(f"Your health: {player['health']}")

                        elif action == "equip":
                            print("\nWeapons you can equip:")

                            #Find weapons in inventory that exist in weapon_stats
                            weapon_options = [item for item in player['inventory'] if item in weapon_stats and item != "Fists"]

                            if not weapon_options:
                                  print("You have no other weapons you can equip.")
                                  print(f"Current weapon: {player['equipped_weapon']} (+{player['weapon_bonus']})\n")
                                  continue
                            for w in weapon_options:
                                  print(f"- {w} (+{weapon_stats[w]})")
                                
                            print()
                            choice = input("Type the name of the weapon that you want to equip: ").strip()

                            if choice in weapon_options:
                                  player['equipped_weapon'] = choice
                                  player['weapon_bonus'] = weapon_stats[choice]
                                  print(f"You equip the {player['equipped_weapon']}.")
                                  print(f"New weapon bonus: + {player['weapon_bonus']} attack\n")
                            else:
                                  print("\nYou fumble with your gear and fail to equip anything.\n")

                            continue
          
                        else:
                            print("You hesitate and do nothing...")

                if player['health'] <= 0:
                    print("You collapse... The darkness takes you.")

                elif monster_health <= 0:
                    print()
                    print("You defeated the monster! Victory is yours!")
                    loot_table = ["Small health potion", "Gold coin", "Rusty sword"]
                    loot = random.choice(loot_table)
                    print(f"The monster dropped: {loot}!")
                    player['inventory'].append(loot)
                    print("You can type 'equip' later to change weapons.")

                    if loot == "Rusty sword":
                          player['equipped_weapon'] = "Rusty sword"
                          player['weapon_bonus'] = 5
                          print("You equip the rusty sword")
                          print(f"Weapon bonus: {player['weapon_bonus']} attack")

                    # EXP REWARD
                    gained_exp = 10
                    exp +=gained_exp
                    print(f"You gained {gained_exp} EXP!")
                    print(f"Total EXP: {exp}/{exp_to_next}")

                    #LEVEL UP CHECK
                    if exp >= exp_to_next:
                          exp -= exp_to_next
                          level += 1
                          player['health'] += 1
                          player['strength'] += 1

                          #Next level takes 5-10 more EXP
                          exp_to_next += random.randint(5,10)

                          print()
                          print(f"*** You leveled up! You are now Level {level}! ***")
                          print(f"Health increased to: {player['health']}")
                          print(f"Strength increased to: {player['strength']}")
                          print(f"Next level at: {exp_to_next} EXP")

          else:
                print("You discover nothing... you continue on.")

else:
    print("You decide to stay in the village another day.")