import random
import os

# Define the base Treasure class


class Treasure:
    """Base class for treasures."""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def pickup(self, player):
        """Pick up the treasure and add its score to the player's score."""
        player.score += self.score

# Define the Gold subclass inheriting from Treasure


class Gold(Treasure):
    """Subclass representing gold treasure."""

    def __init__(self):
        super().__init__("Gold", 50)

# Define the Gems subclass inheriting from Treasure


class Gems(Treasure):
    """Subclass representing gem treasure."""

    def __init__(self):
        super().__init__("Gems", 100)

# Define the Artifacts subclass inheriting from Treasure


class Artifacts(Treasure):
    """Subclass representing artifact treasure."""

    def __init__(self):
        super().__init__("Artifacts", 200)

# Define the Player class


class Player:
    """Class representing the player."""

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.inventory = {'Gold': 0, 'Gems': 0, 'Artifacts': 0}
        self.powers = {
            "Intellect": True,
            "Swordsmanship": True
        }

    def add_treasure(self, treasure):
        """Add treasure to player's inventory."""
        self.inventory[treasure.name] += 1
        self.score += treasure.score

    def inventory_summary(self):
        """Display player's inventory."""
        print("\nInventory Summary:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")
        print(f"Total Score: {self.score}")

# Define the Enemy class


class Enemy:
    """Class representing enemies."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Define the Path class


class Path:
    """Class representing paths."""

    def __init__(self, name, enemy):
        self.name = name
        self.enemy = enemy

    def start_encounter(self, player):
        """Start an encounter with an enemy on the path."""
        print(f"You encounter {self.enemy.name}!")
        print(self.enemy.description)
        player.score += 50  # Reward the player with additional score after each encounter
        print(f"You gained 50 points!")
        # Implement combat mechanics
        if player.powers["Intellect"]:
            print("You use your intellect to outsmart the enemy.")
            print("You successfully defeat the enemy!")
        elif player.powers["Swordsmanship"]:
            print("You use your swordsmanship to engage in combat with the enemy.")
            print("You emerge victorious in battle!")
        else:
            print(
                "You don't have the necessary skills to confront the enemy. You flee the encounter.")

# Define the game class


class SparrowsTreasureHunt:
    def __init__(self):
        self.player = None
        self.high_scores = {"Jack Sparrow": 0, "William Turner": 0}
        self.paths = [
            Path("Path of Barbossa", Enemy("Captain Hector Barbossa",
                                           "You've encountered Captain Hector Barbossa and his cursed crew. Defeat them to proceed!")),
            Path("Path of Davy Jones", Enemy("Davy Jones",
                                             "Davy Jones and the ghostly crew of the Flying Dutchman stand in your way. Outsmart them to continue!")),
            Path("Path of Lord Cutler Beckett", Enemy("Lord Cutler Beckett",
                                                      "Lord Cutler Beckett and his armada threaten your progress. Lead your crew to victory against them!"))
        ]

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        """Display the main menu and handle user input."""
        self.clear_screen()
        while True:
            print("\n=== Main Menu ===")
            print("1. Start Game")
            print("2. View High Scores")
            print("3. Select Profile")
            print("4. Quit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.start_game()
            elif choice == "2":
                self.view_high_scores()
            elif choice == "3":
                self.select_profile()
            elif choice == "4":
                print(
                    "Fare thee well, brave sailor! May your sails be full and your compass true on the next leg of your journey!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")

    def select_profile(self):
        """Allow the player to select a profile."""
        self.clear_screen()
        print("\nSelect Profile:")
        print("1. Jack Sparrow")
        print("2. William Turner")

        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                self.player = Player("Jack Sparrow")
                print("\nWelcome, Jack Sparrow!")
                break
            elif choice == "2":
                self.player = Player("William Turner")
                print("\nWelcome, William Turner!")
                break
            else:
                print("Invalid choice! Please enter 1 or 2.")

    def view_high_scores(self):
        """View high scores."""
        self.clear_screen()
        print("\nHigh Scores:")
        for name, score in self.high_scores.items():
            print(f"{name}: {score}")

    def update_high_scores(self):
        """Update high scores if necessary."""
        if self.player.name in self.high_scores:
            if self.player.score > self.high_scores[self.player.name]:
                self.high_scores[self.player.name] = self.player.score
                print(
                    f"Congratulations! You've set a new high score: {self.player.score}!")
        else:
            self.high_scores[self.player.name] = self.player.score
            print(
                f"Congratulations! You've set a new high score: {self.player.score}!")

    def start_game(self):
        """Start the game."""
        if self.player is None:
            print("Please select a profile first.")
            self.select_profile()
            return

        self.clear_screen()
        print("\nLet's start the adventure!")
        while True:
            print("\nChoose your path:")
            for i, path in enumerate(self.paths, 1):
                print(f"{i}. {path.name}")
            print("4. Exit to Main Menu")

            choice = input("Enter your choice (1-4): ")
            if choice.isdigit() and 1 <= int(choice) <= 3:
                path_index = int(choice) - 1
                self.paths[path_index].start_encounter(self.player)
                self.player.inventory_summary()
            elif choice == "4":
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")

            # Implement end game conditions
            if self.player.score >= 500:
                print("Congratulations! You've completed the quest for lost relics!")
                self.update_high_scores()
                break


# Run the game
if __name__ == "__main__":
    game = SparrowsTreasureHunt()
    game.main_menu()
