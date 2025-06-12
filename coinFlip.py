
import random
from player import Player


class CoinFlip:     
    #TODO: When user enters heads or tails and when coin flip != their option player 2 gets to go first
    #TODO: When heads or tails have it save who goes first // If player 1 picks heads and loses player 2 goes first 
    def headsOrTails(option):
        #Second number = their turn
        player1 = Player(3,0)
        player2 = Player(3,0)

        coin = random.randint(0,1)
       
        option = int(input("Player 1 choose, (0)Heads or (1)Tails?"))
        if coin == 0:
            print("The coinflip decides heads")
            if option != 0:
                player1.turn = -1
                player2.turn = 1
                print(player1.turn)
                print(player2.turn)
        elif coin == 1:
            print("The coinflip decided tails")
            if option != 1:
                player1.turn = -1
                player2.turn = 1
                print(player1.turn)
                print(player2.turn)

        else: 
            print('Error, choose heads or tails / 0 or 1')
            return coinFlip.headsOrTails(option)
        
        return player1, player2