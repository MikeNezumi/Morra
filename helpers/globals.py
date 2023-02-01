import pygame
from pygame.locals import *

LACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (238, 255, 65)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 30
BASIC_FONT_SIZE = 28

pygame.init()
FPS_CLOCK = pygame.time.Clock()
BASIC_FONT = pygame.font.Font('graphics/d-dine.otf', BASIC_FONT_SIZE)
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
