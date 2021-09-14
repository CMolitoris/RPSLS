from Player import Player
import random

class AI(Player):
    def __init__(self,name) -> None:
        super().__init__(name)

    def select_option(self, options):
        AI_input = options[random.randint(0, 4)]
        return AI_input
