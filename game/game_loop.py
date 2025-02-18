# game_loop.py - Controls game flow
from game.constants import INTRO, NAME, DISTRIBUTE_ABILITIES, END
from game.player import create_player, distribute_skill_points, level_up, use_item, change_armor, change_weapon
from game.battle import battle
from game.shop import shop
from game.save_load import save_game, load_game, delete_save, list_saved_games
import os

def game_loop():
    """ Main game loop controlling the flow of the game. """
    player = None

    while True:
        print("\n📂 Welcome to Arkadius --> Text Adventure RPG!")
        print("You will create your own warrior and fight against powerful monsters.")
        print("1 - Start New Game")
        print("2 - Load Saved Game")
        print("3 - Exit Game")
        choice = input("Choose an option: ")

        if choice == "1":
            if player:
                delete_save(player["name"])
            player = None
            break
        elif choice == "2":
            saved_games = list_saved_games()
            if not saved_games:
                print("No saved games found.")
                continue
            for idx, game in enumerate(saved_games, start=1):
                print(f"{idx} - {game}")
            print(f"{len(saved_games) + 1} - Exit to Main Menu")
            load_choice = input("Choose an option: ")
            if load_choice.isdigit() and 1 <= int(load_choice) <= len(saved_games):
                player = load_game(saved_games[int(load_choice) - 1])
                if player:
                    break
                else:
                    print("❌ Error loading game.")
            elif load_choice == str(len(saved_games) + 1):
                continue
        elif choice == "3":
            print("👋 Exiting game.")
            return
        else:
            print("Invalid choice. Please try again.")

    if not player:
        print("\nCreating a new character...")
        player = create_player()
        distribute_skill_points(player["abilities"])

    while True:
        print("\n⚔️ A new battle awaits!")

        print("\n🎒 What do you want to do?")
        print("1 - Fight")
        print("2 - Check inventory")
        print("3 - Exit game")

        action_choice = input("Choose an option: ")

        if action_choice == "1":
            if player["xp"] >= 500:
                print("🔥 A dark presence looms... The Kraken is awakening!")
                result = battle(player, is_boss=True)
                if result == "boss_defeated":
                    print("🎉 You have completed your journey! Congratulations!")
                    break
            battle(player)
        elif action_choice == "2":
            while True:
                print("\n🎒 Inventory Menu")
                print("1 - Use potion")
                print("2 - Change weapon")
                print("3 - Change armor")
                print("4 - Go back")

                inventory_choice = input("Choose an option: ")

                if inventory_choice == "1":
                    use_item(player)
                elif inventory_choice == "2":
                    change_weapon(player)
                elif inventory_choice == "3":
                    change_armor(player)
                elif inventory_choice == "4":
                    break
                else:
                    print("❌ Invalid choice.")
        elif action_choice == "3":
            print("\n💾 Saving game before exit...")
            save_game(player, player["name"])
            print(f"💾 Game saved successfully as {player['name']}! Exiting game.")
            break
        else:
            print("❌ Invalid choice.")

        if level_up(player):
            print(f"🆙 {player['name']} is now stronger and ready for new challenges!")

        if player["abilities"]["Health"]["points"] <= 0:
            print("\n💀 You have been defeated! Game over.")
            delete_save(player["name"])
            break

        print("\n🛒 Do you want to visit the shop?")
        shop_choice = input("1 - Yes, 2 - No: ")
        if shop_choice == "1":
            shop(player)

        print("\n💾 Do you want to save your game before continuing?")
        save_choice = input("1 - Save, 2 - Continue without saving: ")
        if save_choice == "1":
            save_game(player, player["name"])
            print(f"💾 Game saved successfully as {player['name']}!")

        print("\n🔥 Do you want to fight another enemy?")
        continue_choice = input("1 - Yes, 2 - No (Exit Game): ")
        if continue_choice == "2":
            print("\n💾 Saving game before exit...")
            save_game(player, player["name"])
            print(f"💾 Game saved successfully as {player['name']}! Exiting game.")
            break

    print(f"\nGame Over. You finished with {player['gold']} gold, {player['xp']} XP, reached level {player['level']}.")
    print("Thank you for playing! 👋")
