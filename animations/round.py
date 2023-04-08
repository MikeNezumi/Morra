import sys, random, math, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'animations' folder
    from helpers.globals import *
    from helpers.window import loop_footer
    from helpers.misc import keyboard
else:
    pass

def numbers_load(surface):
    keys = [
        [i for i in range(1, 11)], 
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    ]
    key_rects = keyboard(surface, keys, (200, 120))