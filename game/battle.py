import random
import time
from game.loot import award_loot


class Enemy:
    """ Represents an enemy with health, attack power, and special ability. """

    def __init__(self, name, health, attack_power, xp_reward, gold_reward, special_ability):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.special_ability = special_ability

    def attack(self):
        """ Returns the enemy's attack damage. """
        return random.randint(1, self.attack_power)


def get_random_enemy(is_boss=False):
    """ Returns a random enemy with a special ability or a boss. """
    if is_boss:
        return Enemy("Dark Lord", health=100, attack_power=15, xp_reward=100, gold_reward=50,
                     special_ability="Dark Fire")

    enemies = [
        Enemy("Goblin", health=30, attack_power=5, xp_reward=20, gold_reward=10, special_ability="Quick Slash"),
        Enemy("Orc", health=50, attack_power=8, xp_reward=30, gold_reward=15, special_ability="Berserk"),
        Enemy("Skeleton", health=25, attack_power=6, xp_reward=25, gold_reward=12, special_ability="Bone Shield"),
        Enemy("Dark Mage", health=40, attack_power=10, xp_reward=35, gold_reward=20, special_ability="Shadow Bolt")
    ]
    return random.choice(enemies)


def battle(player, is_boss=False):
    """ Handles battles, including loot rewards. """
    enemy = get_random_enemy(is_boss)

    print(f"\n⚔️ You have encountered {enemy.name}!")
    print(
        f"Stats: HP: {enemy.health}, Attack: {enemy.attack_power}, XP Reward: {enemy.xp_reward}, Gold Reward: {enemy.gold_reward}")
    print(f"Special Ability: {enemy.special_ability}")

    fight_choice = input("\nDo you want to enter the fight? (1 - Yes, 2 - No): ")
    if fight_choice != "1":
        print("🏃‍♂️ You decided to avoid the battle.")
        return

    player_health = player["abilities"]["Health"]["points"]

    # Select weapon
    if player["inventory"]["weapons"]:
        current_weapon = player["inventory"]["weapons"][-1]  # Use the last obtained weapon
        weapon_bonus = current_weapon["value"]
        print(f"🗡️ You are using {current_weapon['name']} (+{weapon_bonus} Attack)")
    else:
        weapon_bonus = 0  # No weapon bonus

    player_attack = player["abilities"]["Attack Power"]["points"] + weapon_bonus

    # Select armor
    if player["inventory"]["armor"]:
        current_armor = player["inventory"]["armor"][-1]  # Use the last obtained armor
        armor_bonus = current_armor["value"]
        print(f"🛡️ You are wearing {current_armor['name']} (+{armor_bonus} Defense)")
    else:
        armor_bonus = 0  # No armor bonus

    player_defense = armor_bonus

    print(f"\n⚔️ {player['name']} engages in battle with {enemy.name}!")
    time.sleep(1)

    while player_health > 0 and enemy.health > 0:
        damage = random.randint(1, player_attack)
        enemy.health -= damage
        print(f"💥 You hit {enemy.name} for {damage} damage! {enemy.name} has {max(0, enemy.health)} HP left.")
        time.sleep(1)

        if enemy.health <= 0:
            print(f"🏆 You defeated {enemy.name}!")
            time.sleep(1)
            player["gold"] += enemy.gold_reward
            player["xp"] += enemy.xp_reward

            loot = award_loot(player)  # Player receives loot
            print(f"🎁 {player['name']} received: {loot['name']}!")

            return

        enemy_damage = max(0, enemy.attack() - player_defense)
        player_health -= enemy_damage
        print(f"🔥 {enemy.name} hits you for {enemy_damage} damage! You have {max(0, player_health)} HP left.")
        time.sleep(1)

        if player_health <= 0:
            print("💀 You have been defeated...")
            time.sleep(1)
            break

    print("\nBattle Over.")
    time.sleep(1)
