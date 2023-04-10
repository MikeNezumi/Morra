import pygame
from pygame.locals import *
from array import array

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
MEGA_FONT = pygame.font.Font('graphics/d-dine.otf', 70)
FONTS = [SMALL_FONT, MID_FONT, TITLE_FONT, MEGA_FONT]

DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

NEW_GAME = {
    "even_mode": True,
    "round": 1,
    "even_round": None,
    "target": None,
    "picked": array('i', []),     # a little silly, but arrays are 
    "ai_picked": array('i', []),  # mandated by the assignment
    "score": 0,
    "ai_score": 0,
    "player_rounds": 0,
    "ai_rounds": 0,
    "winner": "You",
    "winner_char": "Eavan"
}

GAME_STATE = {}
GAME_STATE = NEW_GAME.copy()