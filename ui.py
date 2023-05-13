import pygame
import pygame_gui
from constants import Constant, UIDefault
from colorwheel import ColorWheel

class UI:
    def __init__(self, game, renderer):
        self.game = game
        self.game.stepsize = UIDefault.stepsize
        self.renderer = renderer
        self.uiwidth = Constant.uisize*Constant.W
        self.uiheight = Constant.H
        self.uirect = pygame.Rect(Constant.uioffset*Constant.W,0,self.uiwidth,self.uiheight)
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
        self.draw_color_wheel()
        self.renderer.draw_ui(self.manager)

    def draw_color_wheel(self):
        loc = (self.uiwidth//2,500)
        pos = (self.uirect.topleft[0]+loc[0],self.uirect.topleft[1]+loc[1])
        self.renderer.draw_color_wheel(10, pos, hue=(0.2,0.6),sat=(0.8,0.8),value=(1.0,1.0))
