from Gesture import Gesture
from Scissors import Scissors
from Lizard import Lizard

class Rock(Gesture):
    def __init__(self) -> None:
        super().__init__("Rock")    

    # def populate_weaknesses(self):
    #     weakness_one = Scissors()
    #     weakness_two = Lizard()
    #     list_weaknesses = []
    #     return list_weaknesses.extend([weakness_one,weakness_two])
