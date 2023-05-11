import pygame
import pygame_gui
from constants import UIDefault

class Game:
    def __init__(self):
        pass

    def step(self):
        pass

    def update(self, delta):
        for i in range(self.stepsize):
            self.step()