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
        self.dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)] #direction array used for direction id in ants

    def createGrid(self, gw, gh):
        self.grid = SquareGrid(gw, gh)

    #reset the whole game object
    def reset(self):
        self.stepsize = Default.stepsize
        self.createGrid(Default.GW, Default.GH)
        self.createAnts(Default.ants)
        self.createRules(Default.rules, Default.colors)
        self.dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    #create ants with random positions and directions
    def createAnts(self, amount):
        self.ants = []
        for i in range(amount):
            self.ants.append(
                Ant(
                    (
                        random.randint(0, Default.GW - 1),
                        random.randint(0, Default.GH - 1),
                    )
                )
            )

    #randomize ants with random positions and directions
    def randomizeAnts(self):
        for i in range(len(self.ants)):
            self.ants[i] = Ant(
                (random.randint(0, Default.GW - 1), random.randint(0, Default.GH - 1))
            )

    #create rules array from rules string and colors
    def createRules(self, rules, colors):
        self.rules = []
        amount = len(rules)
        for i in range(amount):
            self.rules.append(Rule(rules[i], colors[i]))

    #a single step of the simulation
    def step(self):
        if len(self.rules)==0: return
        for i in range(len(self.ants)):
            ant = self.ants[i]
            x = ant.x
            y = ant.y
            cur_cell = self.grid.getCell(x, y)
            rid = cur_cell.getRuleID()
            cur_rule = self.rules[rid]
            cur_dir = cur_rule.direction_id
            ant.turn(cur_dir, 4)  # rotate ant
            cur_cell.nextRule(len(self.rules))  # apply color to grid
            ant.move(self.dirs)  # move ant forward

        # destroy bad ants
        self.ants = [ant for ant in self.ants if ant.is_alive]

    #each frame update, step X times
    def update(self, delta):
        for i in range(self.stepsize):
            self.step()
