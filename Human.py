from os import truncate
from Player import Player

class Human(Player):
    def __init__(self,name) -> None:
        self.name = name
        super().__init__()

    def select_option(self,options):
        count = 1
<<<<<<< HEAD
=======
        
>>>>>>> 8c21d6a539c8217f1c303be8c4784dedd76a400a
        for option in options:
            print(str(count) + ": " + options.get(option))
            count += 1
        user_input = input("Which would you like to select? ") 
        while True:
            if user_input=="1":
                return "Rock"
            elif user_input=="2":
                return "Scissors"        
            elif user_input=="3":
                return "Paper"    
            elif user_input=="4":
                return "Lizard"    
            elif user_input=="5":
                return "Spock"
            else:
                user_input = input("Invalid input, please select again!")        