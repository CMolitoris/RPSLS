from os import name
from Player import Player

class Human(Player,name):
    def __init__(self) -> None:
        self.name = name
        super().__init__()