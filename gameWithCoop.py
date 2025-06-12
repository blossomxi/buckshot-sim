import player
from coinFlip import *
import random
import time

class GameWithCoop:
    def trackTurn(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
    #Start off with two bullets
    #TODO: Have a system where there can be x amount of duds and legit bullets(?)
    def __init__(self):
        self.bulletCount = 2
        self.dudCount = 0
        self.legitCount = 0
    def Game(self,input):
        #Initialize how many duds and legit in the count randomize?
        # if 2 % x == 0 that equals to legit
        # not then equals to dud
        # we must start we 1 dud 1 legit
        #Initialize round
        round_num = 1
        
        random_number = random.randint(1,100)
        while self.bulletCount != 0:
            if random_number % 2 == 0:
                self.legitCount+=1
                self.bulletCount-=1
            else:
                self.dudCount+=1
                self.bulletCount-=1
        #this makes sure bulletCount =/= 0
        self.bulletCount = self.dudCount + self.legitCount

        print(f"We have {self.bulletCount} in the chamber.")
        print(self.dudCount, self.legitCount)
        while self.bulletCount > 0:
            currentPlayer = self.player1 if self.player1.turn == 1 else self.player2
            otherPlayer = self.player2 if self.player2.turn == 1 else self.player1
            print(f"{'Player 1' if currentPlayer == self.player1 else 'Player 2'}'s turn!")

            action = input("Press 1 to shoot other otherwise press 2 to shoot yourself...")
            time.sleep(0.5)

            #firing a bullet
            #TODO Have logic for when you shoot someone else and it is a dud and have logic when you shoot yourself and it is a dud
            match playerAction:
                case 1:
                    if random_number % 2 == 0:
                        print(f"{'Player 1' if currentPlayer == self.player1 else 'Player 2'} shot {'Player 2' if otherPlayer == self.player2 else 'Player 1'}!")
                        if otherPlayer == self.player2:
                            self.player2.lives -= 1
                        else:
                            self.player1.lives -= 1
                        break
                case 2:
                    if random_number % 2 == 0:
                        print(f"{'Player 1' if currentPlayer == self.player1 else 'Player 2'} shot themselves!")
                        print("It was a dud...")
                case _:
                    print("Error incorrect input")
            

        


        
        

        
    