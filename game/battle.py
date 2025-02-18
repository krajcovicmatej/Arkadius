import random
import time

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

def choose_special_ability():
    """ Allows the player to choose a special battle ability. """
    abilities = {
        "1": {"name": "Power Strike", "effect": "double_attack", "description": "Random chance to deal double damage."},
        "2": {"name": "Defensive Stance", "effect": "reduce_damage",
              "description": "Random chance to take half damage."},
        "3": {"name": "Frenzy", "effect": "extra_hit", "description": "Random chance to strike twice in one turn."}
    }

    print("\n✨ Choose your special battle ability:")
    for key, ability in abilities.items():
        print(f"{key} - {ability['name']}: {ability['description']}")

    while True:
        choice = input("Enter the number of your ability: ")
        if choice in abilities:
            print(f"🎖️ You chose {abilities[choice]['name']}!")
            return abilities[choice]
        else:
            print("Invalid choice! Please enter a valid number.")

def battle(player, is_boss=False):
    """ Handles battles, including special abilities. """
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
    player_attack = player["abilities"]["Attack Power"]["points"] + player["inventory"]["weapon"]["attack_bonus"]
    player_defense = player["inventory"]["armor"]["defense_bonus"]
    special_ability = choose_special_ability()  # Hráč si vyberie špeciálnu schopnosť

    print(f"\n⚔️ {player['name']} engages in battle with {enemy.name}!")
    time.sleep(1)

    while player_health > 0 and enemy.health > 0:
        # Random activation of special ability (25% chance)
        if random.random() < 0.25:
            if special_ability["effect"] == "double_attack":
                print("💥 Your Power Strike activated! You deal double damage!")
                player_attack *= 2
            elif special_ability["effect"] == "reduce_damage":
                print("🛡️ Your Defensive Stance activated! You take half damage this turn!")
                player_defense *= 2
            elif special_ability["effect"] == "extra_hit":
                print("⚡ Your Frenzy activated! You attack twice this turn!")
                extra_attack = random.randint(1, player_attack)
                enemy.health -= extra_attack
                print(f"💥 Extra hit! {enemy.name} takes {extra_attack} damage!")
            time.sleep(1)

        # Player attacks
        damage = random.randint(1, player_attack)
        enemy.health -= damage
        print(f"💥 You hit {enemy.name} for {damage} damage! {enemy.name} has {max(0, enemy.health)} HP left.")
        time.sleep(1)

        if enemy.health <= 0:
            print(f"🏆 You defeated {enemy.name}!")
            time.sleep(1)
            player["gold"] += enemy.gold_reward
            player["xp"] += enemy.xp_reward
            return

        # Enemy attacks
        enemy_damage = max(0, enemy.attack() - player_defense)  # Armor reduces damage
        player_health -= enemy_damage
        print(f"🔥 {enemy.name} hits you for {enemy_damage} damage! You have {max(0, player_health)} HP left.")
        time.sleep(1)

        if player_health <= 0:
            print("💀 You have been defeated...")
            time.sleep(1)
            break

    print("\nBattle Over.")
    time.sleep(1)
