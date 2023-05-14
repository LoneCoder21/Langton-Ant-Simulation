import pygame
import pygame_gui
from constants import Constant, Default
from colorwheel import ColorWheel

class Renderer:
    def __init__(self, game):
        self.game = game
        self.xoff = Default.xoff
        self.yoff = Default.yoff
        self.cellsize = Default.cellsize
        self.window = pygame.Rect(0, 0, Constant.uioffset * Constant.W, Constant.H)
        self.screen = pygame.display.set_mode((Constant.W, Constant.H))
        self.wheel = ColorWheel(Constant.wheelimage, Constant.polarimage, Constant.wheelscale, Constant.polarscale)

    def clearscreen(self):
        pygame.draw.rect(self.screen, Constant.backcolor, self.window)

    def draw_grid(self):
        grid = self.game.grid
        rules = self.game.rules
        for i in range(grid.w):
            for j in range(grid.h):
                colorid = grid.getCell(i,j).getRuleID()
                self.draw_rect(rules[colorid].color, pygame.Rect(self.xoff+i*self.cellsize, self.yoff+j*self.cellsize, self.cellsize, self.cellsize))

    def render(self):
        self.clearscreen()
        self.draw_grid()

    def draw_color_wheel(self, n, pos, hpos, hue, sat, value, color=(0, 0, 0)):
        self.wheel.draw_color_wheel(self.screen, pos)
        self.wheel.draw_help(self.screen, hpos)
        self.wheel.draw_points(self.screen, n, pos, hue, sat, value, color)

    def draw_rect(self, color, rect):
        pygame.draw.rect(self.screen, color, rect)

    def draw_ui(self, uimanager):
        uimanager.draw_ui(self.screen)
