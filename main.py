import random

class player:
    def __init__(self,lives):
        self.lives = lives
class coinFlip:     
    def headsOrTails(input):
        coin = random.randint(1,2)
        print("Heads or Tails")
        input = input()
        if coin == 1:
            print("The coinflip decides heads")
        else:
            print("The coinflip decided tails")


    

    
    
coinFlip.headsOrTails(input)
    
player1 = player(3) 
player2 = player(3)
robot = player(3)

    
        