import pygame
import pygame_gui
from constants import Constant
from colorwheel import ColorWheel


class Renderer:
    def __init__(self):
        self.window = pygame.Rect(0, 0, Constant.uioffset * Constant.W, Constant.H)
        self.screen = pygame.display.set_mode((Constant.W, Constant.H))
        self.wheel = ColorWheel("wheel.png", 250)

    def clearscreen(self):
        pygame.draw.rect(self.screen, Constant.backcolor, self.window)

    def render(self, game):
        self.clearscreen()

    def draw_color_wheel(self, n, pos, hue, sat, value, color=(0, 0, 0), lines=True):
        self.wheel.draw_color_wheel(self.screen, pos)
        self.wheel.draw_points(self.screen, n, pos, hue, sat, value, color, lines)

    def draw_rect(self, color, rect):
        pygame.draw.rect(self.screen, color, rect)

    def draw_ui(self, uimanager):
        uimanager.draw_ui(self.screen)
