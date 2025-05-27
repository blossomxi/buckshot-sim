import random

class player:
    def __init__(self,lives):
        self.lives = lives
class coinFlip:     
    #TODO: When user enters heads or tails and when coin flip != their option player 2 gets to go first
    def headsOrTails(option):
        coin = random.randint(0,1)
        print("Player 1 choose, (0)Heads or (1)Tails?")
        option = input()
        if coin == 0:
            print("The coinflip decides heads")
        elif coin == 1:
            print("The coinflip decided tails")
        else: 
            print('Error, choose heads or tails / 0 or 1')
            return coinFlip.headsOrTails(option)

class gameSelection:
    
    def chooseOption(option):
        #TODO: Allow user to use string aswell
        print("How do you want to play?\n 1.) Co-op\n 2.) AI\n Please choose with 1 or 2")
        option = int(input())
        if option == 1:
            coinFlip.headsOrTails(input)
            print('Going into game now...')
        elif option == 2:
            coinFlip.headsOrTails(input)
            print('Going into game now...')
        elif option != 1 or option !=2:
            print('Error, Please choose 1 or 2.')
        
        
class GameWithCoop:
    #Start off with two bullets
    def game_global():
        global bulletCount
        bulletCount = 2
        player1 = player(3) 
        player2 = player(3)
    def Game(input):
        print("We have" + bulletCount + "in the chamber.")
    
        

    
    
coinFlip.headsOrTails(input)
# gameSelection.chooseOption(input)
    

robot = player(3)

    
        