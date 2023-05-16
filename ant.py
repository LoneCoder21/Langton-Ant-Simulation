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
        # modulo here to cycle around directions in case step count if large

    def move(self, dArray):
        dir = dArray[self.direction]
        self.x += dir[0]
        self.y += dir[1] #update position
        if self.x < 0 or self.x >= Default.GW:
            self.kill()
        if self.y < 0 or self.y >= Default.GH:
            self.kill()
        # no killing
        self.x %= Default.GW
        self.y %= Default.GH
        self.x = (self.x+Default.GW)%Default.GW
        self.y = (self.y+Default.GH)%Default.GH
        #last 4 lines calculate grid wrapping in case of out of grid behavior

    #killing ant replaced with grid wrapping instead
    def kill(self):
        pass
