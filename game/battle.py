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


def battle(player_name, player_abilities):
    """ Manages the battle system between the player and an enemy. """
    enemy = Enemy("Goblin", health=30, attack_power=5)
    player_health = player_abilities["Health"]["points"]
    player_attack = player_abilities["Attack Power"]["points"]

    print(f"\n⚔️ {player_name} encounters a {enemy.name}!")
    print(f"The battle begins! {enemy.name} has {enemy.health} HP.")

    while player_health > 0 and enemy.health > 0:
        print("\nOptions:")
        print("1 - Attack")
        print("2 - Run away")

        choice = input("What will you do? ")

        if choice == "1":
            # Player attacks
            damage = random.randint(1, player_attack)
            enemy.health -= damage
            print(f"💥 You hit the {enemy.name} for {damage} damage!")

            if enemy.health <= 0:
                print(f"🏆 You defeated the {enemy.name}!")
                break

            # Enemy attacks
            enemy_damage = enemy.attack()
            player_health -= enemy_damage
            print(f"🔥 The {enemy.name} hits you for {enemy_damage} damage!")

            if player_health <= 0:
                print("💀 You have been defeated...")
                break

        elif choice == "2":
            print("🏃‍♂️ You ran away!")
            break

        else:
            print("Invalid choice! Try again.")

    print("\nBattle Over.")
