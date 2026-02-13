import pytest
from src.assess_game import Game

@pytest.mark.winningMach
@pytest.mark.parametrize("user, machine, result", [
    ('paper', 'rock', 0),   
    ('scissors','paper' , 0),   
    ('rock','scissors' , 0),   
])
def test_player_wins(user, machine, result):
    game = Game(user, machine,)
    assert game.match() == result 

@pytest.mark.losingMach
@pytest.mark.parametrize("user, machine, result", [
    ('paper', 'siccsors', 1),   
    ('scissors','rock' , 1),   
    ('rock','paper' , 1),   
])
def test_Machine_wins(user, machine, result):
    game = Game(user, machine,)
    assert game.match() == result 

@pytest.mark.foldMach
@pytest.mark.parametrize("user, machine, result", [
    ('paper', 'paper', 2),   
    ('scissors','scissors' , 2),   
    ('rock','rock' , 2),   
])
def test_no_one_wins(user, machine, result):
       game = Game(user, machine,)
       assert game.match() == result 