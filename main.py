from src.assess_game import *

def main():
    game_actions = [ROCK, PAPER, SCISSORS]
    while True:
        user_action = input("\nPick a choice: rock, paper or scissors: ")
        computer_action = random.choice(game_actions)

        print(f"\nYou picked {user_action}. The computer picked {computer_action}\n")
        assess_game(user_action, computer_action)


if __name__ == "__main__":
    main()