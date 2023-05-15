from constants import Default
from rule import Rule
import random

class Ant:
    def __init__(self, position, direction=random.randint(0,3)):
        self.x = position[0]
        self.y = position[1]
        self.direction = direction
        self.is_alive = True

    def turn(self, steps, modAmount):
        self.direction = (self.direction + steps) % modAmount
        self.direction = (self.direction + modAmount) % modAmount

    def move(self, dArray):
        dir = dArray[self.direction]
        self.x += dir[0]
        self.y += dir[1]
        if self.x < 0 or self.x >= Default.GW:
            self.kill()
        if self.y < 0 or self.y >= Default.GH:
            self.kill()
        self.x %= Default.GW
        self.y %= Default.GH
        self.x = (self.x+Default.GW)%Default.GW
        self.y = (self.y+Default.GH)%Default.GH

    def kill(self):
        pass
