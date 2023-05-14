import pygame
import pygame_gui
from constants import Constant, Default
from colorwheel import ColorWheel

class Renderer:
    def __init__(self, game):
        self.game = game
        self.window = pygame.Rect(0, 0, Constant.uioffset * Constant.W, Constant.H)
        self.screen = pygame.display.set_mode((Constant.W, Constant.H))
        self.wheel = ColorWheel("wheel.png", "polar_coords.png")

    def clearscreen(self):
        pygame.draw.rect(self.screen, Constant.backcolor, self.window)

    def draw_grid(self):
        squaregrid = self.game.getgrid()
        for i in range(Default.GW):
            for j in range(Default.GH):
                colorid = squaregrid.get_cell(i,j).getid()
                rules = self.game.getrules()
                self.draw_rect(rules[colorid].color, pygame.Rect(Default.GPX+i*Default.cellsize, Default.GPY+j*Default.cellsize, Default.cellsize, Default.cellsize))

    def render(self):
        self.clearscreen()
        self.draw_grid()

    def draw_color_wheel(self, n, pos, hpos, hue, sat, value, color=(0, 0, 0), lines=True):
        self.wheel.draw_color_wheel(self.screen, pos)
        self.wheel.draw_help(self.screen, hpos)
        self.wheel.draw_points(self.screen, n, pos, hue, sat, value, color, lines)

    def draw_rect(self, color, rect):
        pygame.draw.rect(self.screen, color, rect)

    def draw_ui(self, uimanager):
        uimanager.draw_ui(self.screen)
