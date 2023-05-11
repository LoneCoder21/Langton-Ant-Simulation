import pygame
import pygame_gui
from constants import Constant

class UI:
    def __init__(self, game, renderer):
        self.game = game
        self.renderer = renderer
        self.uirect = pygame.Rect(Constant.uioffset*Constant.W,0,Constant.uisize*Constant.W,Constant.H)
        self.createUI()
        
    def createUI(self):
        self.manager = pygame_gui.UIManager(self.uirect.size)
        self.manager.get_root_container().set_position(self.uirect.topleft)
        
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(0, 0, 100, 80),
                                         text='Grid',
                                         manager=self.manager)

    def eventupdate(self, event):
        if event.ui_element == self.hello_button:
                print('Hello World!')

    def draw(self):
        self.renderer.draw_rect(Constant.uibackcolor, self.uirect)
        self.renderer.draw_ui(self.manager)