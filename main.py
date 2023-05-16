import pygame
import pygame_gui
import renderer
import game
import ui
import rule
import ant
import cell

from constants import Constant

pygame.init()
pygame.display.set_caption(Constant.title)
#initialize pygame

game = game.Game()
renderer = renderer.Renderer(game)
ui = ui.UI(game, renderer)
#initialize all objects

clock = pygame.time.Clock() 
#initialize clock
is_running = True

while is_running:
    time_delta = clock.tick(Constant.FPS)/1000.0
    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

        ui.eventupdate(event)
        ui.manager.process_events(event)

    game.update(time_delta)
    ui.manager.update(time_delta)
    #update game objects and ui
    
    renderer.render()
    ui.draw()
    #draw renderer and UI
    
    pygame.display.update()
    #display screen