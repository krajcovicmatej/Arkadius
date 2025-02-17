# battle.py - Manages the battle system
import random
from player import define_warrior_abilities


class Enemy:
    """ Represents an enemy with health and attack power. """

    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        """ Returns the enemy's attack damage. """
        return random.randint(1, self.attack_power)


def get_random_enemy():
    """ Returns a random enemy from the enemy list. """
    enemies = [
        Enemy("Goblin", health=30, attack_power=5),
        Enemy("Orc", health=50, attack_power=8),
        Enemy("Skeleton", health=25, attack_power=6),
        Enemy("Dark Mage", health=40, attack_power=10)
    ]
    return random.choice(enemies)


def battle(player_name, player_abilities):
    """ Asks the player if they want to fight, then manages the battle. """
    enemy = get_random_enemy()
    player_health = player_abilities["Health"]["points"]
    player_attack = player_abilities["Attack Power"]["points"]

    print(f"\n⚔️ {player_name} encounters a {enemy.name}!")
    print(f"The battle begins! {enemy.name} has {enemy.health} HP. You have {player_health} HP.")

    while True:
        print("\nDo you want to fight or leave?")
        print("1 - Fight")
        print("2 - Leave")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("The battle begins!")
            break
        elif choice == "2":
            print("🏃‍♂️ You decided to leave and avoid the fight.")
            return
        else:
            print("Invalid choice! Please enter 1 to fight or 2 to leave.")

    while player_health > 0 and enemy.health > 0:
        # Player attacks
        damage = random.randint(1, player_attack)
        enemy.health -= damage
        print(f"💥 You hit the {enemy.name} for {damage} damage! {enemy.name} has {max(0, enemy.health)} HP left.")

        if enemy.health <= 0:
            print(f"🏆 You defeated the {enemy.name}!")
            break

        # Enemy attacks
        enemy_damage = enemy.attack()
        player_health -= enemy_damage
        print(f"🔥 The {enemy.name} hits you for {enemy_damage} damage! You have {max(0, player_health)} HP left.")

        if player_health <= 0:
            print("💀 You have been defeated...")
            break

    print("\nBattle Over.")
