import pygame
import pygame_gui
from constants import Constant, Default
from colorwheel import ColorWheel
import random

class UI:
    def __init__(self, game, renderer, running):
        self.game = game
        self.stepsize = Default.stepsize
        self.renderer = renderer
        self.running = running
        self.uiwidth = Constant.uisize * Constant.W
        self.uiheight = Constant.H
        self.uirect = pygame.Rect(Constant.uioffset * Constant.W, 0, self.uiwidth, self.uiheight)
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



def createUI(self):
    self.manager = pygame_gui.UIManager(self.uirect.size)
    self.manager.get_root_container().set_position(self.uirect.topleft)
    
    self.createGridSizeSliders()

    self.createCellSizeSlider()

    self.createMultipleAntsSlider()

    self.createSimulationSpeedSlider()

    self.createRandomizeAntsButton()

    self.createSimulationSpeedButtons()

    self.createRuleUI()

    self.createColorUI()




def createGridSizeSliders(self):
    self.grid_width_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect(10, 50, 200, 30),
        start_value=Default.grid_width,
        value_range=(0, 2000),
        manager=self.manager
    )

    self.grid_height_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect(10, 90, 200, 30),
        start_value=Default.grid_height,
        value_range=(0, 2000),
        manager=self.manager
    )

def createCellSizeSlider(self):
    self.cell_size_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect(10, 130, 200, 30),
        start_value=Default.cell_size,
        value_range=(0, 100),
        manager=self.manager
    )

def createMultipleAntsSlider(self):
    self.multiple_ants_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect(10, 170, 200, 30),
        start_value=Default.multiple_ants,
        value_range=(0, 100),
        manager=self.manager
    )

def createSimulationSpeedSlider(self):
    self.simulation_speed_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect(10, 210, 200, 30),
        start_value=Default.simulation_speed,
        value_range=(0, 2),
        manager=self.manager
    )

def createRandomizeAntsButton(self):
    self.randomize_ants_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(10, 250, 200, 30),
        text='Randomize Ants',
        manager=self.manager
    )

def createSimulationSpeedButtons(self):
    self.simulation_speed_buttons = []
    speed_values = [0.25, 0.5, 1.0, 1.5, 2.0]
    button_width = 40
    button_height = 30
    button_spacing = 10
    x_offset = 10
    y_offset = 290

    for speed in speed_values:
        button_rect = pygame.Rect(x_offset, y_offset, button_width, button_height)
        button = pygame_gui.elements.UIButton(
            relative_rect=button_rect,
            text=f'{speed}x',
            manager=self.manager
        )
        self.simulation_speed_buttons.append(button)
        x_offset += button_width + button_spacing

