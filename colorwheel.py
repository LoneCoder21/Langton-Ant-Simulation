import pygame
import pygame_gui
import math
import cmath
import colorsys

class ColorWheel:
    def __init__(self, img, scale):
        self.wheel = pygame.image.load(img)
        self.wheel = pygame.transform.scale(self.wheel, (scale, scale))
        self.size = self.wheel.get_height()

    def lerp(self,ab,t):
        return ab[0]*t+(1-t)*ab[1]

    def draw_color_wheel(self, screen, pos):
        pos=(pos[0]-self.size//2,pos[1]-self.size//2)
        screen.blit(self.wheel, pos)

    def draw_points(self, screen, n, pos, hue, sat, value, color, lines=True, radius=2):
        points = self.get_points(n,pos,hue,sat,value)
        for i in range(0, n):
            pygame.draw.circle(screen, color, points[i], radius)
            
        if lines:
            for i in range(1,n):
                pygame.draw.line(screen, color, points[i-1], points[i], radius-1)

    def get_points(self, n, pos, hue, sat, value):
        pos=(pos[0]-self.size//2,pos[1]-self.size//2)
        points=[]
        for i in range(0, n):
            t = float(i)/(n)
            h,s,v = self.lerp(hue,t), self.lerp(sat,t), self.lerp(value,t)
            cp = cmath.rect(s, h*2.0*math.pi)
            loc = (pos[0]+self.size//2+cp.real*(self.size//2), pos[1]+self.size//2+cp.imag*(self.size//2))
            points.append(loc)
        return points

    def get_rgb_colors(self, n, hue, sat, value):
        rgb_points=[]
        for i in range(0, n):
            t = float(i)/(n)
            h,s,v = self.lerp(hue,t), self.lerp(sat,t), self.lerp(value,t)
            rgb = colorsys.hsv_to_rgb(h,s,v)
            rgb = (int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255))
            rgb_points.append(rgb)
        return rgb_points