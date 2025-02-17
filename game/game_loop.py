# game_loop.py - Controls game flow
from constants import INTRO, NAME, DISTRIBUTE_ABILITIES, END
from game.player import create_player, distribute_skill_points
from game.battle import battle
from game.shop import shop

def game_loop():
    current_phase = INTRO
    player = {}
    battles_won = 0

    while current_phase != END:
        if current_phase == INTRO:
            print("Welcome to the Arkadius --> Text Adventure RPG!")
            print("You will create your own warrior and fight against powerful monsters.")
            input("Press Enter to continue...")
            current_phase = NAME

        elif current_phase == NAME:
            player = create_player()
            current_phase = DISTRIBUTE_ABILITIES


        elif current_phase == DISTRIBUTE_ABILITIES:

            distribute_skill_points(player["abilities"])

            current_phase = "BATTLE_LOOP"


        elif current_phase == "BATTLE_LOOP":

            while True:


                is_boss_fight = battles_won > 0 and battles_won % 3 == 0

                battle(player, is_boss_fight)

                if player["abilities"]["Health"]["points"] <= 0:
                    print("\n💀 You have been defeated! Game over.")

                    current_phase = END

                    break

                battles_won += 1

                print("\n🛒 Do you want to visit the shop?")

                shop_choice = input("1 - Yes, 2 - No: ")

                if shop_choice == "1":
                    shop(player)

                print("\n🔥 Do you want to fight another enemy?")

                continue_choice = input("1 - Yes, 2 - No: ")

                if continue_choice == "2":
                    print("\n👋 You decide to leave the battlefield and rest.")

                    current_phase = END

                    break

    print(f"\nGame Over. You finished with {player['gold']} gold, {player['xp']} XP, reached level {player['level']}, and won {battles_won} battles.")

    print("Thank you for playing! 👋")

