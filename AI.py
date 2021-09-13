from Player import Player
import random

class AI(Player):
    def __init__(self,name) -> None:
        super().__init__(name)

    def select_option(self, options):

        AI_input = options[random.randint(0, 4)]
        return AI_input

        # while True:
        #     if AI_input=="1":
        #         return "Rock"
        #     elif AI_input=="2":
        #         return "Scissors"        
        #     elif AI_input=="3":
        #         return "Paper"    
        #     elif AI_input=="4":
        #         return "Lizard"    
        #     elif AI_input=="5":
        #         return "Spock"