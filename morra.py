import sys, math, random, pygame
from pygame.locals import *
from helpers.globals import *
from helpers.window import check_for_quit, loop_footer
from helpers.process import evaluate
from animations.title import wait_for_start
from animations.char_pick import char_fade, char_pick, char_chosen
from animations.round import numbers_load, round_result
from animations.results import results


# Todo: inplement properly
def main():
    global DISPLAY_SURFACE, GAME_STATE
    wait_for_start(DISPLAY_SURFACE)     # slide 1
    
    char_fade(DISPLAY_SURFACE)          # slide 2 - animation
    # slide 2 - choice:
    GAME_STATE["even_mode"] = char_pick(DISPLAY_SURFACE) 
    char_chosen(DISPLAY_SURFACE)        # slide 2 - chosen animation
    
    round_over = False
    while not round_over:  # a round
        numbers_load(DISPLAY_SURFACE)   # slide 3
        round_over = evaluate()         # slide 3 - anyone 6 points?
        
        round_result(DISPLAY_SURFACE)   # slide 4
        GAME_STATE["round"] += 1

    results(DISPLAY_SURFACE)            # slide 5 #TODO
    check_for_quit()

if __name__ == '__main__':
    main()
