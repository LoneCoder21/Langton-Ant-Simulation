import pygame
import pygame_gui
from constants import Update

class Game:
    def __init__(self):
        pass

    def step(self):
        pass

    def update(self, delta):
        for i in range(Update.stepsize):
            self.step()