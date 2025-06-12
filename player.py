
class Player:
    def __init__(self,lives,turn):
        self.lives = lives
        self.turn = turn #This will be how we decide who goes first
    # gives user attack
    def attack(self):
        damage = 1
    # misses if it was a dude
    def miss(self):
        damage = 0
