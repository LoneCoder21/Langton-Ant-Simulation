import pygame
import pygame_gui
import math
import cmath

class ColorWheel:
    def __init__(self):
        pass

    def polar_to_rect(self, size, h, s):
        size2 = size//2
        cp = cmath.rect(s, h)
        return (size2+cp.real*size2,size2+cp.imag*size2)

    def draw_color_wheel(self, screen):
        wheel = pygame.image.load('wheel.png')
        wheel = pygame.transform.scale(wheel, (250, 250))
        screen.blit(wheel, (0,0))
        wh = wheel.get_height()
        frac = 0.5
        off = 0.5
        n = 10
        for i in range(0, n):
            pygame.draw.circle(screen, (255,255,255), self.polar_to_rect(wh,float(i)/(n-1)*math.pi*2.0*frac+off*2.0*math.pi,0.8), 2)