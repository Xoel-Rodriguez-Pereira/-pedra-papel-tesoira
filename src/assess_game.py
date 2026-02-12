# Listado 1.13: Implementación base del juego piedra, papel o tijeras.

#!/usr/bin/python3

from src.game_actions import GameActions


def assess_game(user_action, computer_action): 
    if user_action == computer_action:
        print(f"User and computer picked {user_action}. Draw game!")

    # You picked Rock
    elif user_action == GameActions.ROCK.value:
        if computer_action in GameActions.WINING_MATCHES.value[user_action]:
            print(f"Rock smashes {computer_action}. You won!") 
        else:
            print(f"{computer_action.title()} covers rock. You lost!")
    
    # You picked Paper
    elif user_action == GameActions.PAPER.value:
        if computer_action in GameActions.WINING_MATCHES.value[user_action]:
            print(f" Paper covers {computer_action}. You won!") 
        else:
            print(f"{computer_action.title()} cut paper. You lost!")
    
    # You picked Scissors
    elif user_action == GameActions.SCISSORS.value:
        if computer_action in GameActions.WINING_MATCHES.value[user_action]:
            print(f" Siccsors cut {computer_action}. You won!") 
        else:
            print(f"{computer_action.title()} smash sicssors. You lost!")

