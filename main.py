import random
from src.assess_game import *
from src.game_actions import GameActions
from src.control_errors import IncorrectOptionException
def main():
    game_actions = [GameActions.ROCK.value, GameActions.PAPER.value, GameActions.SCISSORS.value]

    while True:
        user_action = input("\nPick a choice: rock, paper or scissors: ")
        computer_action = random.choice(game_actions)

        if IncorrectOptionException.isInputValid(user_action):
            print(f"\nYou picked {user_action}. The computer picked {computer_action}\n")
            assess_game(user_action, computer_action)
        else: 
            print(f"\nYou picked {user_action}. That is not a valid action")


if __name__ == "__main__":
    main()