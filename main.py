def start_game():
    """
    Displays the introduction text and waits for player input.
    """
    print("Welcome to the Arkadius --> Text Adventure RPG!")
    print("You will create your own warrior and fight against powerful monsters.")

    while True:
        print("\nAre you ready to play?")
        print("1 - Yes, start the game")
        print("0 - No, exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Great! Let's begin...")
            break
        elif choice == "0":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 1 to start or 0 to exit.")

    name = choose_warrior_name()
    abilities = define_warrior_abilities(name)
    distribute_skill_points(abilities)


def choose_warrior_name():
    """
    Asks the player to choose a name for their warrior.
    """
    while True:
        name = input("Enter your warrior's name: ")
        print(f"You chose the name: {name}")
        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm == "yes":
            print(f"Welcome, {name}! Your adventure begins now.")
            return name
        else:
            print("Let's choose another name.")


def define_warrior_abilities(name):
    """
    Defines the warrior's abilities with initial values.
    """
    abilities = {
        "Attack Power": {"points": 1, "description": "Determines your damage output in battle."},
        "Defense": {"points": 1, "description": "Reduces incoming damage from enemies."},
        "Agility": {"points": 1, "description": "Affects dodge chances and attack speed."},
        "Skill": {"points": 1, "description": "Increases critical hit chances and accuracy."},
        "Health": {"points": 50, "description": "Represents your life points in battle."},
        "Luck": {"points": 1, "description": "Influences critical hit rates and rare loot drops."}
    }

    print(f"\n{name}, here are your initial abilities:")
    for ability, stats in abilities.items():
        print(f"{ability}: {stats['points']} points - {stats['description']}")

    return abilities


def distribute_skill_points(abilities):
    """
    Allows the player to distribute additional skill points.
    """
    available_points = 7

    while available_points > 0:
        print(f"\nYou have {available_points} skill points to distribute.")
        print("Choose an ability to improve:")
        for i, ability in enumerate(abilities.keys(), 1):
            print(f"{i} - {ability} ({abilities[ability]['points']} points)")

        choice = input("Enter the number of the ability to upgrade: ")

        try:
            choice = int(choice)
            ability_list = list(abilities.keys())
            if 1 <= choice <= len(ability_list):
                selected_ability = ability_list[choice - 1]
                if selected_ability == "Health":
                    abilities[selected_ability]["points"] += 5
                else:
                    abilities[selected_ability]["points"] += 1
                available_points -= 1
                print(f"You added a point to {selected_ability}!")
            else:
                print("Invalid choice. Please select a valid ability.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nFinal abilities:")
    for ability, stats in abilities.items():
        print(f"{ability}: {stats['points']} points")
    print("\nYou are now ready for battle!")


start_game()
