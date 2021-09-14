from Player import Player

class Human(Player):
    def __init__(self,name) -> None:
        super().__init__(name)

    def select_option(self,options):
        count = 1
        for option in options:
            print(str(count) + ": " + option.name)
            count += 1
        user_input = input("Which would you like to select? ") 
        while True:
            if user_input=="1":
                return self.options[0]
            elif user_input=="2":
                return self.options[1]        
            elif user_input=="3":
                return self.options[2]    
            elif user_input=="4":
                return self.options[3]    
            elif user_input=="5":
                return self.options[4]
            else:
                user_input = input("Invalid input, please select again!")        