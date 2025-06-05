from player import *
from coinFlip import *
import random

class GameWithCoop:
    def trackTurn(self, p1, p2):
        self.player1 = p1
        self.palyer2 = p2
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
        


        
        

        
    