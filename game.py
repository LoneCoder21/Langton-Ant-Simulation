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
        self.createGrid(Default.GW, Default.GH)
        self.createAnts(Default.ants)
        self.createRules(Default.rules, Default.colors)

    def createGrid(self, gw, gh):
        self.grid = SquareGrid(gw, gh)

    def createAnts(self, amount):
        self.ants = []
        for i in range(amount):
            self.ants.append(Ant((random.randint(0, Default.GW), random.randint(0, Default.GH))))

    def randomizeAnts(self):
        for i in range(len(self.ants)):
            self.ants[i] = Ant((random.randint(0, Default.GW), random.randint(0, Default.GH)))

    def createRules(self, rules, colors):
        self.rules = []
        amount = len(rules)
        for i in range(amount):
            self.rules.append(Rule(rules[i], colors[i]))

    def step(self):
        pass

    def update(self, delta):
        for i in range(self.stepsize):
            self.step()
