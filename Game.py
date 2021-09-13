from Human import Human
from Player import Player
from AI import AI
import random
from Colors import Color

class Game:
    def __init__(self) -> None:
        self.color = Color()
        self.options = {}
        self.players = []
        self.choose_players()
        self.populate_options()
        self.run_game()

    # Display rules to user (best of 3, what beats what, etc.)
    # Human v Human or Human v AI
    # System that checks input against each other
    # Determine who won
    # Continue until one wins two matches


    
    
    def run_game(self):
        self.display_rules()
        self.match_sequence()
        
    def display_rules(self):
        print('\33[32m' + "Observe the following:" + '\33[0m')
        print("\nRock crushes Scissors"
            + "\nScissors cuts Paper"
            + "\nPaper covers Rock"
            + "\nRock crushes Lizard"
            + "\nLizard poisons Spock"
            + "\nSpock smashes Scissors"
            + "\nScissors decapitates Lizard"
            + "\nLizard eats Paper"
            + "\nPaper disproves Spock"
            + "\nSpock vaporizes Rock"
            )
        print("\nIf the gesture you select defeats the opponent's selected gesture, you gain a point." 
            + "\nFirst to 2 points, wins the match!")    

    def match_sequence(self):
        done = False
        while not done:
            player_one_choice = self.players[0].select_option(self.options)
            player_two_choice = self.players[1].select_option(self.options)
            
            
            self.contest(player_one_choice, player_two_choice)
            done = self.check_who_won()

    def check_who_won(self):
        player_one = self.players[0]
        player_two = self.players[1]
        if player_one.points==2:
            self.display_winners(player_one)
            return True
        if player_two.points==2:
            self.display_winners(player_two)
            return True    
        return False

    def display_winners(self,player):
        print("\n" + player.name + " has won the match!")

    #-- PVE/PVP --#
    def choose_players(self):
        print("1: Player Vs Player\n2: Player Vs AI")
        selection = input("Which one would you like? ")
        valid = False
        while not valid:
            if selection=="1":
                valid = True
            elif selection=="2":
                valid = True
            else:
                selection = input("Invalid input, please select again: ")
        self.populate_players(selection)

    def populate_options(self):
        update = {"1":"Rock","2":"Scissors","3":"Paper","4":"Lizard","5":"Spock"}
        self.options.update(update)

    def populate_players(self,selection):
        if selection=="1":
            player_one_name = input("Enter Player one's name: ")
            player_two_name = input("Enter Player two's name: ")
            self.players.append(Human(player_one_name))
            self.players.append(Human(player_two_name))
        else:
            player_one_name = input("Enter Player One's name: ")
            self.players.append(Human(player_one_name)) 
            self.players.append(AI())
            
    def contest(self,player_one_option,player_two_option):
        print("\n" + self.players[0].name + " has selected " + player_one_option + "!")
        print(self.players[1].name + " has selected " + player_two_option + "!")
        option_dictionary = {"Rock":["Scissors","Lizard"],"Scissors":["Paper","Lizard"],"Paper":["Rock","Spock"],"Lizard":["Spock","Paper"],"Spock":["Scissors","Rock"]}
        list_gestures_weakness = option_dictionary.get(player_one_option)
        if player_one_option == player_two_option:
            print("Draw! Both gestures were the same!")
        else:
            if player_two_option != list_gestures_weakness[0] and player_two_option != list_gestures_weakness[1]:
                print(self.players[1].name + " gets a point!")
                self.players[1].points += 1
            else: 
                print(self.players[0].name + " gets a point!")
                self.players[0].points += 1        
        
