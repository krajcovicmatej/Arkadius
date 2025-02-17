# game_loop.py - Controls game flow
def game_loop():
    current_phase = INTRO
    name = ""
    abilities = {}

    while current_phase != END:
        if current_phase == INTRO:
            print("Welcome to the Text Adventure RPG!")
            print("You will create your own warrior and fight against powerful monsters.")
            input("Press Enter to continue...")
            current_phase = NAME
        elif current_phase == NAME:
            name = choose_warrior_name()
            abilities = define_warrior_abilities()
            current_phase = DISTRIBUTE_ABILITIES
        elif current_phase == DISTRIBUTE_ABILITIES:
            distribute_skill_points(abilities)
            current_phase = END

    print("Game Over. Thank you for playing!")

