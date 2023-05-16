import pygame
import pygame_gui
import math
import cmath
import colorsys

class ColorWheel:
    def __init__(self, img, help, sw, sh):
        self.wheel = pygame.image.load(img)
        self.wheel = pygame.transform.scale(self.wheel, (sw, sw))
        self.help = pygame.image.load(help)
        self.help = pygame.transform.scale(self.help, (sh, sh))
        self.helpsize = self.wheel.get_width()
        self.size = self.wheel.get_height()
        #create images from path and scale them

    def draw_help(self, screen, pos):
        screen.blit(self.help, pos)
        #draw help image

    def draw_color_wheel(self, screen, pos):
        pos=(pos[0]-self.size//2,pos[1]-self.size//2)        
        screen.blit(self.wheel, pos)
        #draw color wheel image

    #draw the points that appear on the color model
    def draw_points(self, screen, n, pos, hue, sat, value, color, lines=True, radius=2):
        points = self.get_points(n,pos,hue,sat,value)
        for i in range(1, n-1): #draw all points except 1st and last
            pygame.draw.circle(screen, color, points[i], radius)
        if n>=1: #draw 1st point
            pygame.draw.circle(screen, (255-color[0],255-color[1],255-color[2]), points[0], radius+2)
        if n>=2: #draw last point
            pygame.draw.circle(screen, color, points[-1], radius+2)

        if lines: #draw lines between points
            for i in range(1,n):
                pygame.draw.line(screen, color, points[i-1], points[i], radius-1)
            #pygame.draw.line(screen, color, points[-1], points[0], radius-1)

    #get point positions in cartesian coordinate space
    def get_points(self, n, pos, hue, sat, value):
        pos=(pos[0]-self.size//2,pos[1]-self.size//2)
        points=[]
        for i in range(0, n):
            t = float(i)/(n)
            h,s,v = ColorWheel.lerp(hue,t), ColorWheel.lerp(sat,t), ColorWheel.lerp(value,t)
            cp = cmath.rect(s, h*2.0*math.pi)
            loc = (pos[0]+self.size//2+cp.real*(self.size//2), pos[1]+self.size//2+cp.imag*(self.size//2))
            points.append(loc)
        points.reverse()
        return points

    #linear interpolation
    @staticmethod
    def lerp(ab,t):
        return ab[0]*t+(1-t)*ab[1]

    #get rgb colors
    @staticmethod
    def get_rgb_colors(n, hue, sat, value):
        rgb_points=[]
        for i in range(0, n):
            t = float(i)/(n)
            h,s,v = ColorWheel.lerp(hue,t), ColorWheel.lerp(sat,t), ColorWheel.lerp(value,t) #linear interpolation between the hue, sat, and value ranges
            rgb = colorsys.hsv_to_rgb(h,s,v)
            rgb = (int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255))
            rgb = (min(255, max(0, rgb[0])), min(255, max(0, rgb[1])), min(255, max(0, rgb[2]))) #in case of overflow or underflow
            rgb_points.append(rgb)
        rgb_points.reverse()
        return rgb_points