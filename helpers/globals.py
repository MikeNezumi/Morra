import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (237, 239, 0)
BLACK_A = 120

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 30
BASIC_FONT_SIZE = 28

pygame.init()
FPS_CLOCK = pygame.time.Clock()
BASIC_FONT = pygame.font.Font('graphics/d-dine.otf', BASIC_FONT_SIZE)
SMALL_FONT = pygame.font.Font('graphics/d-dine.otf', 16)
MID_FONT = pygame.font.Font('graphics/d-dine.otf', 25)
TITLE_FONT = pygame.font.Font('graphics/d-dine.otf', 45)
FONTS = [SMALL_FONT, MID_FONT, TITLE_FONT]

DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

GAME_STATE = {
    "even_mode": None
}