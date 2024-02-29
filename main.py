import random
import os


# Define the base Treasure class

class Treasure:
    def __init__(self):
        self.score = 0

    def pickup(self, player):
        """Pick up the treasure and add its score to the player's score."""
        player.score += self.score

# Define the Gold subclass inheriting from Treasure


class Gold(Treasure):
    def __init__(self):
        super().__init__()
        self.score = 50

    def pickup(self, player):
        """Pick up the gold treasure, add its score to the player's score, and increase the gold count in the player's inventory."""
        super().pickup(player)
        player.treasures['Gold'] += 1

# Define the Player, Enemy, and Path classes


class Player:
    def __init__(self):
        """Initialize the player's attributes."""
        self.gold = 0
        self.gems = {}
        self.artifacts = []
        self.powers = {
            "Intellect": True,
            "Escape Artist": True,
            "Gadgets": True,
            "Leadership": True,
            "Swordsmanship": True
        }

    def add_gem(self, name, value):
        """Add a gem to the player's inventory."""
        if name in self.gems:
            self.gems[name] += value
        else:
            self.gems[name] = value

    def activate_artifact(self, artifact):
        """Activate an artifact and add it to the player's inventory."""
        self.artifacts.append(artifact)
        print(f"You've acquired {artifact.name} with power {artifact.power}!")

    def display_inventory(self):
        """Display the player's inventory."""
        print("Inventory:")
        print("Gold:", self.gold)
        print("Gems:", self.gems)
        print("Artifacts:", [artifact.name for artifact in self.artifacts])

    def use_power(self, power):
        """Check if the player has a specific power."""
        if power in self.powers:
            return self.powers[power]
        else:
            return False


class Enemy:
    def __init__(self, name, description):
        """Initialize the enemy with a name and description."""
        self.name = name
        self.description = description


class Path:
    def __init__(self, name, enemy):
        """Initialize the path with a name and enemy."""
        self.name = name
        self.enemy = enemy

    def start_encounter(self, player):
        """Start an encounter with an enemy on the path."""
        print(f"You encounter {self.enemy.name}!")
        print(self.enemy.description)
        player.display_inventory()


class SparrowsTreasureHunt:
    def __init__(self):
        """Initialize the game with a player and paths."""
        self.player = Player()
        self.paths = [
            Path("Path of Barbossa", Enemy("Captain Hector Barbossa",
                 "You've encountered Captain Hector Barbossa and his cursed crew. Defeat them to proceed!")),
            Path("Path of Davy Jones", Enemy(
                "Davy Jones", "Davy Jones and the ghostly crew of the Flying Dutchman stand in your way. Outsmart them to continue!")),
            Path("Path of Lord Cutler Beckett", Enemy("Lord Cutler Beckett",
                 "Lord Cutler Beckett and his armada threaten your progress. Lead your crew to victory against them!"))
        ]

    def start_game(self):
        """Start the game and display the main menu."""
        print("Welcome to the Jack Sparrow's Treasure Hunt!")
        while True:
            try:
                enter_game = input("Do you want to enter? (y/n): ").lower()
                if enter_game == 'y':
                    self.main_menu()
                elif enter_game == 'n':
                    print(
                        "As you wish, matey! Fare thee well on your journey across the seas!")
                    break
                else:
                    raise ValueError("Invalid input! Please enter 'y' or 'n'.")
            except ValueError as e:
                print(f"Error: {e}")

    def main_menu(self):
        """Display the main menu and handle user input."""
        print("\n=== Main Menu ===")
        print("1. Start Game")
        print("2. View High Scores")
        print("3. Select Profile")
        print("4. Quit")

        try:
            choice = input("Enter your choice: ")
            if choice == "1":
                self.start_treasure_hunt()
            elif choice == "2":
                self.view_high_scores()
            elif choice == "3":
                self.select_profile()
            elif choice == "4":
                print(
                    "Fare thee well, brave sailor! May your sails be full and your compass true on the next leg of your journey!")
                quit()
            else:
                raise ValueError(
                    "Invalid choice! Please enter a number between 1 and 4.")
        except ValueError as e:
            print(f"Error: {e}")

    def start_treasure_hunt(self):
        """Start the treasure hunt by choosing a path and encountering an enemy."""
        print("Jack Sparrow sets sail in search of treasure...")

        # Choose a random path for the player
        current_path = random.choice(self.paths)
        print(f"You've chosen the {current_path.name}.")

        # Start encounter with enemy on the chosen path
        current_path.start_encounter(self.player)

        # to be continued .... stay tuned!


# Call the clear_screen function before starting the game
def clear_screen():
    """Clears the terminal screen."""
    # Clear screen command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear screen command for Unix/Linux/MacOS
    else:
        os.system('clear')


clear_screen()


# Testing the game
game = SparrowsTreasureHunt()
game.start_game()
