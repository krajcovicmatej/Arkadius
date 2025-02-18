import random

SHOP_ITEMS = {
    "weapons": [
        {"name": "Iron Sword", "attack_bonus": 5, "base_price": 50},
        {"name": "Steel Sword", "attack_bonus": 10, "base_price": 100},
        {"name": "Dragon Slayer", "attack_bonus": 20, "base_price": 250}
    ],
    "armor": [
        {"name": "Leather Armor", "defense_bonus": 3, "base_price": 40},
        {"name": "Iron Armor", "defense_bonus": 7, "base_price": 90},
        {"name": "Dragon Scale Armor", "defense_bonus": 15, "base_price": 200}
    ],
    "potions": [
        {"name": "Small Health Potion", "heal_amount": 20, "base_price": 20},
        {"name": "Large Health Potion", "heal_amount": 50, "base_price": 50}
    ]
}


def get_dynamic_price(item, player_level):
    """ Adjusts the price of an item based on the player's level. """
    return item["base_price"] + (player_level * 5)


def shop(player):
    """ Allows the player to buy or sell items. """
    while True:
        print("\n🛒 Welcome to the Shop!")
        print("1 - Buy Items")
        print("2 - Sell Items")
        print("3 - Exit Shop")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\n💰 Available Items:")
            items_for_sale = []
            for category, items in SHOP_ITEMS.items():
                for item in items:
                    price = get_dynamic_price(item, player["level"])
                    items_for_sale.append((item, category, price))
                    print(f"{len(items_for_sale)} - {item['name']} (Price: {price} gold)")

            item_choice = input("\nEnter the number of the item to buy (or 0 to cancel): ")
            if item_choice.isdigit():
                item_choice = int(item_choice)
                if 1 <= item_choice <= len(items_for_sale):
                    item, category, price = items_for_sale[item_choice - 1]
                    if player["gold"] >= price:
                        player["gold"] -= price
                        player["inventory"][category].append(item)
                        print(f"✅ You bought {item['name']}!")
                    else:
                        print("❌ You don't have enough gold.")
                elif item_choice == 0:
                    continue
                else:
                    print("❌ Invalid selection.")
            else:
                print("❌ Invalid input.")

        elif choice == "2":
            sell_item(player)

        elif choice == "3":
            print("👋 Thank you for visiting!")
            break
        else:
            print("❌ Invalid choice.")


def sell_item(player):
    """ Allows the player to sell items for gold. """
    inventory_items = []

    for category, items in player["inventory"].items():
        for item in items:
            sell_price = get_dynamic_price(item, player["level"]) // 2  # Polovičná cena pri predaji
            inventory_items.append((item, category, sell_price))

    if not inventory_items:
        print("❌ You have nothing to sell.")
        return

    print("\n🛒 Items you can sell:")
    for idx, (item, category, price) in enumerate(inventory_items, start=1):
        print(f"{idx} - {item['name']} (Sell Price: {price} gold)")

    sell_choice = input("\nEnter the number of the item to sell (or 0 to cancel): ")
    if sell_choice.isdigit():
        sell_choice = int(sell_choice)
        if 1 <= sell_choice <= len(inventory_items):
            item, category, price = inventory_items[sell_choice - 1]
            player["gold"] += price
            player["inventory"][category].remove(item)
            print(f"✅ You sold {item['name']} for {price} gold!")
        elif sell_choice == 0:
            return
        else:
            print("❌ Invalid selection.")
    else:
        print("❌ Invalid input.")
