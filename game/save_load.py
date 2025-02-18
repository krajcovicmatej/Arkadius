import json
import os

SAVE_DIR = "saves/"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


def save_game(player, filename):
    """ Saves the current state of the player to a file named after the player's hero. """
    save_path = os.path.join(SAVE_DIR, f"{filename}.json")
    try:
        with open(save_path, "w") as file:
            json.dump(player, file, indent=4)
        print(f"💾 Game saved successfully as {filename}!")
    except Exception as e:
        print(f"❌ Error saving game: {e}")


def load_game(filename):
    """ Loads the game state from a file if it exists. """
    save_path = os.path.join(SAVE_DIR, f"{filename}.json")
    if not os.path.exists(save_path):
        print("❌ Save file not found.")
        return None

    try:
        with open(save_path, "r") as file:
            player = json.load(file)
        print(f"📂 Game loaded successfully from {filename}!")
        return player
    except Exception as e:
        print(f"❌ Error loading game: {e}")
        return None


def delete_save(filename=None):
    """ Deletes a specific save file or all saves if no filename is provided. """
    if filename:
        save_path = os.path.join(SAVE_DIR, f"{filename}.json")
        if os.path.exists(save_path):
            os.remove(save_path)
            print(f"🗑️ Save file {filename} deleted. Starting a new game!")
    else:
        for file in os.listdir(SAVE_DIR):
            if file.endswith(".json"):
                os.remove(os.path.join(SAVE_DIR, file))
        print("🗑️ All save files deleted. Starting a new game!")



def list_saved_games():
    """ Returns a list of available saved game files. """
    saves = [f.split(".json")[0] for f in os.listdir(SAVE_DIR) if f.endswith(".json")]
    return saves
