import pygame
import pygame_gui
from constants import Constant

class Renderer:
    def __init__(self, W, H):
        self.screen = pygame.display.set_mode((W, H))

        self.background = pygame.Surface((W, H))
        self.background.fill(pygame.Color(Constant.backcolor))

        self.ui_background = pygame.Surface((W, H))
        self.ui_background.fill(pygame.Color(Constant.uibackcolor))
        
    def draw(self):
        self.screen.blit(self.background, (0, 0))
    
        #drawing begin
        
        #drawing end
        
        self.screen.blit(self.ui_background, (Constant.uioffset * Constant.W, 0))