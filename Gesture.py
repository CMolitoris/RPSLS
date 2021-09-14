
class Gesture:
    def __init__(self,name) -> None:
        self.name = name
        self.weaknesses = self.generate_weaknesses()

    def compare_gestures(self,players,player_two_option):
        if self.name == player_two_option.name:
            print("Draw! Both gestures were the same!")
        else:
            if player_two_option.name == self.weaknesses[0] or player_two_option.name == self.weaknesses[1]:
                print(players[0].name + " gets a point!\n")
                players[0].points += 1
            else: 
                print(players[1].name + " gets a point!\n")
                players[1].points += 1   

    def generate_weaknesses(self):
        list = []
        if self.name == "Rock":
            list.extend(["Scissors","Lizard"])
            return list
        elif self.name == "Scissors":
            list.extend(["Paper","Lizard"])
            return list
        elif self.name == "Paper":
            list.extend(["Rock","Spock"])
            return list
        elif self.name == "Lizard":
            list.extend(["Spock","Paper"])
            return list
        elif self.name == "Spock":
            list.extend(["Scissors","Rock"])
            return list










