# player.py - Handles player creation and attributes
from game.loot import award_loot  # Import pre loot systém

def choose_warrior_name():
    while True:
        name = input("Enter your warrior's name: ")
        print(f"You chose the name: {name}")
        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm == "yes":
            print(f"Welcome, {name}! Your adventure begins now.")
            return name
        else:
            print("Let's choose another name.")

def define_warrior_abilities():
    return {
        "Attack Power": {"points": 1, "description": "Determines your damage output in battle."},
        "Defense": {"points": 1, "description": "Reduces incoming damage from enemies."},
        "Agility": {"points": 1, "description": "Affects dodge chances and attack speed."},
        "Skill": {"points": 1, "description": "Increases critical hit chances and accuracy."},
        "Health": {"points": 50, "description": "Represents your life points in battle."},
        "Luck": {"points": 1, "description": "Influences critical hit rates and rare loot drops."}
    }

def choose_special_ability():
    """ Allows the player to choose a special ability. """
    abilities = {
        "1": {"name": "Power Strike", "effect": "double_attack", "description": "Deals double damage in one attack."},
        "2": {"name": "Healing Light", "effect": "heal", "description": "Restores 20 HP."},
        "3": {"name": "Lucky Shot", "effect": "critical_hit", "description": "Guaranteed critical hit."}
    }

    print("\n✨ Choose a special ability:")
    for key, ability in abilities.items():
        print(f"{key} - {ability['name']}: {ability['description']}")

    while True:
        choice = input("Enter the number of your ability: ")
        if choice in abilities:
            print(f"🎖️ You chose {abilities[choice]['name']}!")
            return abilities[choice]
        else:
            print("Invalid choice! Please enter a valid number.")

def create_player():
    """ Creates a player with initial attributes including gold, XP, level, and inventory. """
    return {
        "name": choose_warrior_name(),
        "abilities": define_warrior_abilities(),
        "special_ability": choose_special_ability(),  # Hráč si vyberie špeciálnu schopnosť pri vytvorení
        "gold": 0,
        "xp": 0,
        "level": 1,
        "inventory": {
            "weapons": [],
            "armor": [],
            "potions": [],
            "special": []
        }
    }

def level_up(player):
    """ Increases the player's level when enough XP is collected. """
    xp_needed = player["level"] * 100  # XP required for next level

    if player["xp"] >= xp_needed:
        player["level"] += 1
        player["xp"] -= xp_needed

        print(f"\n🎉 Level Up! {player['name']} is now level {player['level']}!")

        # Bonusy pri levelovaní
        player["abilities"]["Health"]["points"] += 5
        player["abilities"]["Attack Power"]["points"] += 2
        player["gold"] += 50  # Extra zlato
        loot = award_loot(player)  # Extra loot
        print(f"💰 You received 50 gold and a special reward: {loot['name']}!")

        return True

    return False
def use_item(player):
    """ Allows the player to use healing potions from the inventory. """
    potions = player["inventory"]["potions"]

    if not potions:
        print("❌ You have no potions to use.")
        return

    print("\n🧪 Your potions:")
    for idx, potion in enumerate(potions, start=1):
        print(f"{idx} - {potion['name']} (+{potion['value']} HP)")

    choice = input("Enter the number of the potion to use (or 0 to cancel): ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(potions):
            potion = potions.pop(choice - 1)  # Remove used potion from inventory
            player["abilities"]["Health"]["points"] += potion["value"]
            print(f"✨ You used {potion['name']} and restored {potion['value']} HP!")
        elif choice == 0:
            print("❌ Action canceled.")
        else:
            print("❌ Invalid selection.")
    else:
        print("❌ Invalid input.")

def change_weapon(player):
    """ Allows the player to change weapons in the inventory. """
    weapons = player["inventory"]["weapons"]

    if not weapons:
        print("❌ You have no weapons to equip.")
        return

    print("\n🗡️ Your weapons:")
    for idx, weapon in enumerate(weapons, start=1):
        print(f"{idx} - {weapon['name']} (+{weapon['value']} Attack)")

    choice = input("Enter the number of the weapon to equip (or 0 to cancel): ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(weapons):
            player["inventory"]["weapons"].append(player["inventory"]["weapons"].pop(choice - 1))  # Move weapon to last position
            print(f"🔄 You equipped {weapons[-1]['name']}!")
        elif choice == 0:
            print("❌ Action canceled.")
        else:
            print("❌ Invalid selection.")
    else:
        print("❌ Invalid input.")

def change_armor(player):
    """ Allows the player to change armor in the inventory. """
    armor = player["inventory"]["armor"]

    if not armor:
        print("❌ You have no armor to equip.")
        return

    print("\n🛡️ Your armor pieces:")
    for idx, armor_piece in enumerate(armor, start=1):
        print(f"{idx} - {armor_piece['name']} (+{armor_piece['value']} Defense)")

    choice = input("Enter the number of the armor to equip (or 0 to cancel): ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(armor):
            player["inventory"]["armor"].append(player["inventory"]["armor"].pop(choice - 1))  # Move armor to last position
            print(f"🔄 You equipped {armor[-1]['name']}!")
        elif choice == 0:
            print("❌ Action canceled.")
        else:
            print("❌ Invalid selection.")
    else:
        print("❌ Invalid input.")

def distribute_skill_points(abilities, available_points=7):
    """ Allows the player to distribute skill points. """
    while available_points > 0:
        print(f"\nYou have {available_points} skill points to distribute.")
        print("Choose an ability to improve:")
        for i, ability in enumerate(abilities.keys(), 1):
            print(f"{i} - {ability} ({abilities[ability]['points']} points)")

        choice = input("Enter the number of the ability to upgrade: ")

        try:
            choice = int(choice)
            ability_list = list(abilities.keys())
            if 1 <= choice <= len(ability_list):
                selected_ability = ability_list[choice - 1]
                if selected_ability == "Health":
                    abilities[selected_ability]["points"] += 5
                else:
                    abilities[selected_ability]["points"] += 1
                available_points -= 1
                print(f"You added a point to {selected_ability}!")
            else:
                print("Invalid choice. Please select a valid ability.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nFinal abilities:")
    for ability, stats in abilities.items():
        print(f"{ability}: {stats['points']} points")
    print("\nYou are now ready for battle!")
