from game_actions import GameActions
class IncorrectOptionException():
    def isInputValid(user_action):
        try:
            if user_action in list(GameActions):
                return True
            else:
                return False
        except:
            return False