#!/usr/bin/env python3
from player import *
from coinFlip import CoinFlip
from gameWithCoop import GameWithCoop
        
def main():
    player1, player2 = CoinFlip.headsOrTails(option=input)
    
    gameCoop = GameWithCoop()

    gameCoop.trackTurn(player1, player2)
    gameCoop.Game(input)


    
if __name__ == "__main__":
    main()