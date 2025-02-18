import random

LOOT_TABLE = {
    "common": [
        {"name": "Small Health Potion", "effect": "heal", "value": 20},
        {"name": "Rusty Dagger", "effect": "weapon", "value": 2},
        {"name": "Old Shield", "effect": "armor", "value": 1},
    ],
    "rare": [
        {"name": "Large Health Potion", "effect": "heal", "value": 50},
        {"name": "Steel Sword", "effect": "weapon", "value": 5},
        {"name": "Iron Armor", "effect": "armor", "value": 3},
    ],
    "legendary": [
        {"name": "Excalibur", "effect": "weapon", "value": 10},
        {"name": "Dragon Scale Armor", "effect": "armor", "value": 7},
        {"name": "Phoenix Feather", "effect": "revive", "value": 1},
    ]
}


def get_loot():
    """ Randomly selects loot based on drop chances. """
    loot_roll = random.random()

    if loot_roll < 0.6:  # 60% šanca na bežný loot
        return random.choice(LOOT_TABLE["common"])
    elif loot_roll < 0.9:  # 30% šanca na vzácny loot
        return random.choice(LOOT_TABLE["rare"])
    else:  # 10% šanca na legendárny loot
        return random.choice(LOOT_TABLE["legendary"])


def award_loot(player):
    """ Awards loot to the player after a successful battle. """
    loot = get_loot()
    print(f"🎁 You found: {loot['name']}!")

    if loot["effect"] == "heal":
        player["inventory"]["potions"].append(loot)
    elif loot["effect"] == "weapon":
        player["inventory"]["weapons"].append(loot)
    elif loot["effect"] == "armor":
        player["inventory"]["armor"].append(loot)
    elif loot["effect"] == "revive":
        player["inventory"]["special"].append(loot)

    return loot
