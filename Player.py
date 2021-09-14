from Scissors import *
from Rock import *
from Lizard import *
from Paper import *
from Spock import *

class Player:
    def __init__(self,name) -> None:
        self.options = []
        self.name = name
        self.points = 0
        self.populate_options()

    def select_option(self):
        pass

    def populate_options(self):
        update = [Rock(),Scissors(),Paper(),Lizard(),Spock()]
        self.options.extend(update)
