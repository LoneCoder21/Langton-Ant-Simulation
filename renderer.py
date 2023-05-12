import pygame
import pygame_gui
from constants import Constant
from colorwheel import ColorWheel

class Renderer:
    def __init__(self):
        self.window = pygame.Rect(0,0,Constant.uioffset*Constant.W,Constant.H)
        self.screen = pygame.display.set_mode((Constant.W, Constant.H))

    def clearscreen(self):
        pygame.draw.rect(self.screen, Constant.backcolor, self.window)

    def render(self, game):
        self.clearscreen()
        self.draw_color_wheel()

    def draw_color_wheel(self):
        wheel = ColorWheel()

    def draw_rect(self, color, rect):
        pygame.draw.rect(self.screen, color, rect)

    def draw_ui(self, uimanager):
        uimanager.draw_ui(self.screen)