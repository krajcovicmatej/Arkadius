def shop(player):
    """ Allows the player to spend gold on upgrades. """
    print("\n💰 Welcome to the shop!")
    print(f"You have {player['gold']} gold.")

    items = {
        "1": {"name": "Increase Attack Power (+1)", "cost": 10, "stat": "Attack Power", "value": 1},
        "2": {"name": "Increase Defense (+1)", "cost": 10, "stat": "Defense", "value": 1},
        "3": {"name": "Increase Health (+10)", "cost": 15, "stat": "Health", "value": 10},
        "4": {"name": "Exit shop", "cost": 0}
    }

    while True:
        print("\nShop items:")
        for key, item in items.items():
            print(f"{key} - {item['name']} ({item['cost']} gold)")

        choice = input("Enter the number of the item you want to buy: ")

        if choice in items:
            if choice == "4":
                print("👋 You leave the shop.")
                break

            item = items[choice]
            if player["gold"] >= item["cost"]:
                player["gold"] -= item["cost"]
                player["abilities"][item["stat"]]["points"] += item["value"]
                print(
                    f"🎉 You bought {item['name']}! Your {item['stat']} is now {player['abilities'][item['stat']]['points']}.")
            else:
                print("❌ You don't have enough gold!")

        else:
            print("Invalid choice! Please enter a valid number.")
