import pygame
from pygame.locals import *

def backlit_rect(surface, points, alpha):  # from list of 4 points, creates black rect backlight
    width = abs(points[1][0] - points[0][0])
    height = abs(points[2][1] - points[1][1])
    s = pygame.Surface((width, height))
    s.set_alpha(alpha)               
    s.fill((0,0,0))           
    surface.blit(s, points[0])