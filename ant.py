from constants import Default
from rule import Rule


class Ant:
    def __init__(self, position, direction):
        # self.id = id
        self.position = position
        self.direction = direction
        self.is_alive = True

    def turn(self, steps, modAmount):
        self.steps = steps
        direction = (direction + steps) % modAmount
        direction = (direction + modAmount) % modAmount

    def move(self, dArray):
        dir = dArray[self.direction]
        self.position[0] += dir[0]
        self.position[1] += dir[1]
        if self.position[0] < 0 or self.position[0] >= Default.GW:
            self.kill()
        if self.position[1] < 0 or self.position[1] >= Default.GH:
            self.kill()

    def isit_alive(self):
        return self.is_alive

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def kill(self):
        self.is_alive = False
