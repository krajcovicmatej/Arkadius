import time
import random

from game.player import define_warrior_abilities
from game.player import check_level_up
from game.player import choose_special_ability

class Enemy:
    """ Represents an enemy with health and attack power. """
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        """ Returns the enemy's attack damage. """
        return random.randint(1, self.attack_power)


class Boss(Enemy):
    """ Represents a powerful boss enemy. """

    def __init__(self):
        super().__init__("Dark Lord", health=100, attack_power=15)


def get_random_enemy(is_boss=False):
    """ Returns a random enemy from the enemy list or a boss. """
    if is_boss:
        return Boss()

    enemies = [
        Enemy("Goblin", health=30, attack_power=5),
        Enemy("Orc", health=50, attack_power=8),
        Enemy("Skeleton", health=25, attack_power=6),
        Enemy("Dark Mage", health=40, attack_power=10)
    ]
    return random.choice(enemies)


def battle(player, is_boss=False):
    """ Handles battles, including boss fights. """
    enemy = get_random_enemy(is_boss)
    player_health = player["abilities"]["Health"]["points"]
    player_attack = player["abilities"]["Attack Power"]["points"]

    print(f"\n⚔️ {player['name']} encounters {'the mighty' if is_boss else 'a'} {enemy.name}!")
    print(f"The battle begins! {enemy.name} has {enemy.health} HP. You have {player_health} HP.")
    time.sleep(1)

    special_ability = choose_special_ability()  # Hráč si vyberie špeciálnu schopnosť
    ability_used = False  # Sleduje, či hráč schopnosť už použil

    while player_health > 0 and enemy.health > 0:
        print("\nChoose an action:")
        print("1 - Normal Attack")
        print("2 - Use Special Ability" if not ability_used else "❌ Special Ability Used")

        action_choice = input("Enter your choice: ")

        if action_choice == "2" and not ability_used:
            if special_ability["effect"] == "double_attack":
                damage = random.randint(1, player_attack) * 2
                print("💥 You unleash a powerful strike!")
            elif special_ability["effect"] == "heal":
                player_health += 20
                print("✨ You healed yourself for 20 HP!")
                damage = 0  # Healing does not attack
            elif special_ability["effect"] == "critical_hit":
                damage = player_attack * 2
                print("🎯 You land a critical hit!")

            ability_used = True  # Označíme schopnosť ako použitú
        else:
            damage = random.randint(1, player_attack)

        enemy.health -= damage
        print(f"💥 You hit {enemy.name} for {damage} damage! {enemy.name} has {max(0, enemy.health)} HP left.")
        time.sleep(1)

        if enemy.health <= 0:
            print(f"🏆 You defeated {enemy.name}!")
            time.sleep(1)

            # Reward the player
            gold_reward = random.randint(10, 50) if is_boss else random.randint(5, 20)
            xp_reward = random.randint(30, 100) if is_boss else random.randint(10, 30)
            player["gold"] += gold_reward
            player["xp"] += xp_reward

            print(f"🎉 You earned {gold_reward} gold and {xp_reward} XP!")
            time.sleep(1)

            # Check if the player can level up
            check_level_up(player)
            return

        # Enemy attacks
        enemy_damage = enemy.attack()
        player_health -= enemy_damage
        print(f"🔥 {enemy.name} hits you for {enemy_damage} damage! You have {max(0, player_health)} HP left.")
        time.sleep(1)

        if player_health <= 0:
            print("💀 You have been defeated...")
            time.sleep(1)
            break

    print("\nBattle Over.")
    time.sleep(1)