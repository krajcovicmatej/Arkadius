def shop(player):
    """ Allows the player to spend gold on upgrades. """
    print("\n💰 Welcome to the shop!")
    print(f"You have {player['gold']} gold.")

    items = {
        "1": {"name": "Iron Sword", "cost": 15, "type": "weapon", "attack_bonus": 3},
        "2": {"name": "Steel Sword", "cost": 30, "type": "weapon", "attack_bonus": 5},
        "3": {"name": "Leather Armor", "cost": 20, "type": "armor", "defense_bonus": 2},
        "4": {"name": "Chainmail", "cost": 40, "type": "armor", "defense_bonus": 5},
        "5": {"name": "Exit shop", "cost": 0}
    }

    while True:
        print("\nShop items:")
        for key, item in items.items():
            print(f"{key} - {item['name']} ({item['cost']} gold)")

        choice = input("Enter the number of the item you want to buy: ")

        if choice in items:
            if choice == "5":
                print("👋 You leave the shop.")
                break

            item = items[choice]
            if player["gold"] >= item["cost"]:
                player["gold"] -= item["cost"]

                if item["type"] == "weapon":
                    player["inventory"]["weapon"] = {"name": item["name"], "attack_bonus": item["attack_bonus"]}
                elif item["type"] == "armor":
                    player["inventory"]["armor"] = {"name": item["name"], "defense_bonus": item["defense_bonus"]}

                print(f"🎉 You bought {item['name']}!")
            else:
                print("❌ You don't have enough gold!")

        else:
            print("Invalid choice! Please enter a valid number.")
