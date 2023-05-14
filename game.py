import pygame
import pygame_gui
import random

from constants import Default
import rule
import cell


from rule import Rule
from squaregrid import SquareGrid
from ant import Ant


class Game:
    def __init__(self):
        self.stepsize = Default.stepsize
        self.rules = [Rule((0, 0, 0), "R"), Rule((255, 255, 255), "L")]
        self.grid = SquareGrid(Default.GW, Default.GH)
        self.ants = [Ant((Default.GW // 2, Default.GH // 2), 1)]
        pass

    def gridSlider(self):
        self.grid = SquareGrid(Default.GW, Default.GH)

    def antSlider(self):
        self.ants = []
        for i in range(Default.ants):
            self.ants.append(
                Ant(
                    (random.randint(0, Default.GW), random.randint(0, Default.GH)),
                    random.randint(0, 4),
                )
            )

    def randomAnts(self):
        for i in range(Default.ants):
            self.ants[i] = Ant(
                (random.randint(0, Default.GW), random.randint(0, Default.GH)),
                random.randint(0, 4),
            )

    def inputRule(self):
        self.rules = []
        for i in range(len(Default.rules)):
            self.rules.append(Rule((0, 0, 0), Default.rules[i]))

    def step(self):
        pass

    def update(self, delta):
        for i in range(self.stepsize):
            self.step()
