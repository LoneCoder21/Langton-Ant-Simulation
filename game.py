import pygame
import pygame_gui
from constants import Default

class Game:
    def __init__(self):
        self.stepsize = Default.stepsize

    def step(self):
        pass

    def update(self, delta):
        for i in range(self.stepsize):
            self.step()