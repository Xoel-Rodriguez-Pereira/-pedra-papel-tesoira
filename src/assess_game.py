# Listado 1.13: Implementación base del juego piedra, papel o tijeras.

#!/usr/bin/python3

import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

def assess_game(user_action, computer_action): 
    if user_action == computer_action:
        print(f"User and computer picked {user_action}. Draw game!")

    # You picked Rock
    elif user_action == ROCK:
        if computer_action == SCISSORS:
            print("Rock smashes scissors. You won!") 
        else:
            print("Paper covers rock. You lost!")
    
    # You picked Paper
    elif user_action == PAPER:
        if computer_action == ROCK:
            print("Paper covers rock. You won!")
        else:
            print("Scissors cuts paper. You lost!")
    
    # You picked Scissors
    elif user_action == SCISSORS:
        if computer_action == ROCK:
            print("Rock smashes scissors. You lost!") 
        else:
            print("Scissors cuts paper. You won!")

