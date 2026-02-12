from enum import Enum

class GameActions(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    WINING_MATCHES = {
        'rock': ('scissors'),
        'paper': ('rock'),
        'scissors': ('paper'),
    }



