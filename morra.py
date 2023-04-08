import sys, math, random, pygame
from pygame.locals import *
from helpers.globals import *
from helpers.window import terminate, check_for_quit, loop_footer
from animations.title import wait_for_start
from animations.char_pick import char_fade, char_pick, char_chosen
from animations.round import numbers_load


# Todo: inplement properly
def main():
    global DISPLAY_SURFACE, GAME_STATE
    #wait_for_start(DISPLAY_SURFACE) # slide 1
    #char_fade(DISPLAY_SURFACE)      # slide 2 - animation
    # slide 2 - choice:
    GAME_STATE["even_mode"] = char_pick(DISPLAY_SURFACE) 
    char_chosen(DISPLAY_SURFACE)    # slide 2 - chosen animation
    numbers_load(DISPLAY_SURFACE) # slide 2 - buttons drop animation
    while True:
        loop_footer()
    check_for_quit()

if __name__ == '__main__':
    main()
