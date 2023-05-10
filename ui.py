import pygame
import pygame_gui

class UI:
    def __init__(self, W, H, uioffset):
        self.manager = pygame_gui.UIManager((W, H))
        self.manager.get_root_container().set_position((uioffset*W,0))
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(0, 0, 100, 80),
                                         text='Grid',
                                         manager=self.manager)
    def eventupdate(self, event):
        if event.ui_element == self.hello_button:
                print('Hello World!')
        self.manager.process_events(event)