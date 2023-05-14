import pygame
import pygame_gui
from constants import Constant, Default
from colorwheel import ColorWheel
import random

class UI:
    def __init__(self, game, renderer):
        self.game = game
        self.stepsize = Default.stepsize
        self.renderer = renderer
        self.uiwidth = Constant.uisize*Constant.W
        self.uiheight = Constant.H
        self.uirect = pygame.Rect(Constant.uioffset*Constant.W,0,self.uiwidth,self.uiheight)
        self.createUI()
        
    def createUI(self):
        self.manager = pygame_gui.UIManager(self.uirect.size)
        self.manager.get_root_container().set_position(self.uirect.topleft)
        
        self.hello_button = pygame_gui.elements.UIButton(
                                        relative_rect=pygame.Rect(0, 0, 100, 80),
                                        text='Grid',
                                        manager=self.manager)

        self.createColorUI()

    def eventupdate(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.hello_button:
                print('Grid button pressed!')
        self.coloreventupdate(event)

    def coloreventupdate(self, event):
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == self.huestart:
                self.draw_color_wheel()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.randomize_colors_button:
                self.huestart.set_current_value(random.uniform(-0.5,1.5))
                self.hueend.set_current_value(random.uniform(-0.5,1.5))
                self.satstart.set_current_value(random.uniform(0.2,1.0))
                self.satend.set_current_value(random.uniform(0.2,1.0))
                self.valuestart.set_current_value(random.uniform(0.5,1.0))
                self.valueend.set_current_value(random.uniform(0.5,1.0))

    def draw(self):
        self.renderer.draw_rect(Constant.uibackcolor, self.uirect)
        self.draw_color_wheel()
        self.renderer.draw_ui(self.manager)

    def draw_color_wheel(self):
        loc = (self.uiwidth//2, 500)
        pos = (self.uirect.topleft[0]+loc[0],self.uirect.topleft[1]+loc[1])
        hpos = (self.uirect.topleft[0]+0,self.uirect.topleft[1]+550)
        self.renderer.draw_color_wheel(10, pos, hpos,
                                hue=(self.huestart.get_current_value(),self.hueend.get_current_value()),
                                sat=(self.satstart.get_current_value(),self.satend.get_current_value()),
                                value=(self.valuestart.get_current_value(),self.valueend.get_current_value()))

    def createColorUI(self):
        label_y_offset = 22
        ystart = 650
        huestartlabel =  pygame_gui.elements.UILabel(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart-label_y_offset,self.uiwidth*0.9, 30),
                                        text='Hue Start',
                                        manager=self.manager
                                        )
        hueoff=0.5
        self.huestart = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart,self.uiwidth*0.9, 30),
                                        start_value=0.0,
                                        value_range=(0.0-hueoff, 1.0+hueoff),
                                        click_increment=0.1,
                                        manager=self.manager)
        ystart+=50
        hueendlabel =  pygame_gui.elements.UILabel(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart-label_y_offset,self.uiwidth*0.9, 30),
                                        text='Hue End',
                                        manager=self.manager
                                        )

        self.hueend = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart,self.uiwidth*0.9, 30),
                                        start_value=1.0,
                                        value_range=(0.0-hueoff, 1.0+hueoff),
                                        click_increment=0.1,
                                        manager=self.manager)

        ystart+=50
        satstartlabel =  pygame_gui.elements.UILabel(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart-label_y_offset,self.uiwidth*0.9, 30),
                                        text='Sat Start',
                                        manager=self.manager
                                        )

        self.satstart = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart,self.uiwidth*0.9, 30),
                                        start_value=0.5,
                                        value_range=(0.0, 1.0),
                                        click_increment=0.1,
                                        manager=self.manager)
        ystart+=50
        satendlabel =  pygame_gui.elements.UILabel(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart-label_y_offset,self.uiwidth*0.9, 30),
                                        text='Sat End',
                                        manager=self.manager
                                        )

        self.satend = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart,self.uiwidth*0.9, 30),
                                        start_value=0.5,
                                        value_range=(0.0, 1.0),
                                        click_increment=0.1,
                                        manager=self.manager)
        
        ystart+=50
        valuestartlabel =  pygame_gui.elements.UILabel(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart-label_y_offset,self.uiwidth*0.9, 30),
                                        text='Value Start',
                                        manager=self.manager
                                        )

        self.valuestart = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart,self.uiwidth*0.9, 30),
                                        start_value=1.0,
                                        value_range=(0.0, 1.0),
                                        click_increment=0.1,
                                        manager=self.manager)
        ystart+=50
        valueendlabel =  pygame_gui.elements.UILabel(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart-label_y_offset,self.uiwidth*0.9, 30),
                                        text='Value End',
                                        manager=self.manager
                                        )

        self.valueend = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
                                        relative_rect=pygame.Rect((self.uiwidth*0.1)//2,ystart,self.uiwidth*0.9, 30),
                                        start_value=1.0,
                                        value_range=(0.0, 1.0),
                                        click_increment=0.1,
                                        manager=self.manager)
        ystart+=30
        bw = 180
        self.randomize_colors_button = pygame_gui.elements.UIButton(
                                        relative_rect=pygame.Rect((self.uiwidth-bw)//2, ystart, bw, 26),
                                        text='Randomize Colors',
                                        manager=self.manager)