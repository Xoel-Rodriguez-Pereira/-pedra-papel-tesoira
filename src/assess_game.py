# Listado 1.13: Implementación base del juego piedra, papel o tijeras.

#!/usr/bin/python3
from enum import Enum
from src.game_actions import GameActions

class Game:

    def __init__(self, user_action, computer_action):
        self.user_action = user_action
        self.computer_action = computer_action
        self.WINING_MATCHES = {
            'rock': ('scissors'),
            'paper': ('rock'),
            'scissors': ('paper'),
        }
        self.result = 2

    def assess_game(self): 
        if self.result == GameResult.draw:
            print(f"User and computer picked {self.user_action}. Draw game!")

        # You picked Rock
        elif self.result == GameResult.computerWins:
            print(f"{self.computer_action.title()} wins {self.user_action}. You lost!")
        
        # You picked Paper
        else:
            print(f"{self.user_action.title()} wins {self.computer_action}. You win!")

    def match(self):
        if self.user_action == self.computer_action:
            self.result = GameResult.draw

        elif self.computer_action in self.WINING_MATCHES[self.user_action]:
            self.result = GameResult.playerWins
        
        else:
            self.result = GameResult.computerWins

        return self.result.value

class GameResult(Enum):
    playerWins = 0
    computerWins = 1
    draw = 2
