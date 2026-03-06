# Aletheria Pause Menu for base exploration and combat.

from typing import Callable, Optional

def pause_menu(
    player: dict,
    show_stats_fn: Optional[Callable[[dict], None]] = None,
    equip_fn: Optional[Callable[[dict], None]] = None,
    human_item_fn: Optional[Callable[[str], str]] = None,
    save_fn: Optional[Callable[[dict], None]] = None,
) -> str:
    def print_inventory():
        print("\nYour Inventory:")
        inv = player.get("inventory", [])
        if inv:
            for item in inv:
                label = human_item_fn(item) if human_item_fn else item
                print(f"- {label}")
        else:
            print("  (empty)")
        print()

    while True:
        print("\n=== Pause Menu ===")
        print("play / 1 - Resume")
        print("inv / 2 - View Inventory")
        print("stats / 3 - Check Status")
        print("equip - Equip Weapon")
        print("save / 4 - Save Game (soon)")
        print("quit / 5 - Exit Game")
        print("help / 6 - Help")

        choice = input("Choose: ").strip().lower()

        if choice in ("play", "resume", "1"):
            return "resume"
        if choice in ("inv", "inventory", "2"):
            print_inventory()
            continue
        if choice in ("stats", "status", "3"):
            if show_stats_fn:
                show_stats_fn(player)
            else:
                print(f"\nPlayer Stats: {player}\n")
            continue
        if choice in ("equip", "e"):
            if equip_fn:
                equip_fn(player)
            else:
                print("Equip not wired yet.")
            continue
        if choice in ("save", "4"):
            if save_fn:
                save_fn(player)
                print("\nGame saved.\n")
            else:
                print("\nSave not wired yet.\n")
            continue
        if choice in ("quit", "exit", "5"):
            if save_fn:
                confirm = input("Save before quitting? (yes/no): ").strip().lower()
                if confirm in ("yes", "y"):
                    save_fn(player)
                    print("\nGame saved.\n")
            return "quit"
        if choice in ("help", "6", "?"):
            print("Commands: play, inv, stats, equip, save, quit")
            continue

        print("Unrecognized menu option. Type 'help'.")