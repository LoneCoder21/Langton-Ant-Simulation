from constants import Default
from rule import Rule
import random

class Ant:
    def __init__(self, position, direction=random.randint(0,3)):
        self.position = position
        self.direction = direction
        self.is_alive = True

    def turn(self, steps, modAmount):
        self.direction = (self.direction + steps) % modAmount
        self.direction = (self.direction + modAmount) % modAmount

    def move(self, dArray):
        dir = dArray[self.direction]
        self.position[0] += dir[0]
        self.position[1] += dir[1]
        if self.position[0] < 0 or self.position[0] >= Default.GW:
            self.kill()
        if self.position[1] < 0 or self.position[1] >= Default.GH:
            self.kill()

    def kill(self):
        self.is_alive = False
