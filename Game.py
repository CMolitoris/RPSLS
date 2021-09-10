from Human import Human
from Player import Player
from AI import AI


class Game:
    def __init__(self) -> None:
        self.options = {}
        self.players = []
        self.choose_players()
        self.populate_options()
        pass

    # Display rules to user (best of 3, what beats what, etc.)
    # Human v Human or Human v AI
    # System that checks input against each other
    # Determine who won
    # Continue until one wins two matches


    
    
    def run_game(self):
        pass

    def display_rules(self):
        pass

    def match_sequence(self):
        pass

    def check_who_won(self):
        pass

    #-- PVE/PVP --#
    def choose_players(self):
        print("1: Player Vs Player\n2: Player Vs AI")
        selection = input()
        valid = False
        while not valid:
            if selection=="1":
                valid = True
                pass
            elif selection=="2":
                valid = True
                pass
            else:
                selection = input("Invalid input, please select again: ")
        self.populate_players(selection)

    def populate_options(self):
        update = {"1":"Rock","2":"Scissors","3":"Paper","4":"Lizard","5":"Spock"}
        self.options.update(update)

    def populate_players(self,selection):
        if selection=="1":
            player_one_name = input("Enter Player One's name:")
            player_two_name = input("Enter Player Two's name: ")
            self.players.append(Human(player_one_name))
            self.players.append(Human(player_two_name))
        else:
            player_one_name = input("Enter Player One's name:")
            self.players.append(Human(player_one_name)) 
            self.players.append(AI())
            