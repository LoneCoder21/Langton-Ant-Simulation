import pygame
import pygame_gui
from constants import UIDefault
import rule
import ant
import cell


from rule import Rule
from squaregrid import SquareGrid


class Game:
    def __init__(self):
        self.rule = Rule()
        self.rules = [rule((0, 0, 0), "R"), rule((255, 255, 255), "L")]
        self.grid = SquareGrid()
        pass

    def step(self):
        pass

    def update(self, delta):
        for i in range(self.stepsize):
            self.step()
