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

game = game.Game()
renderer = renderer.Renderer()
ui = ui.UI(game, renderer)
clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(Constant.FPS)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            ui.eventupdate(event)

        ui.manager.process_events(event)

    game.update(time_delta)
    ui.manager.update(time_delta)
    
    renderer.render(game)
    ui.draw()
    
    pygame.display.update()