from src.game_actions import GameActions

class IncorrectOptionException():

    def isInputValid(user_action):
        if user_action in [action.value for action in GameActions]:
            return True
        else:
            return False
