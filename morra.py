import sys, math, random, pygame
from pygame.locals import *
from helpers.globals import *
from helpers.window import check_for_quit, loop_footer
from helpers.process import evaluate, save_winners, reset_round
from animations.title import wait_for_start
from animations.char_pick import char_fade, char_pick, char_chosen
from animations.round import numbers_load, round_result
from animations.results import round_results, play_again, overall_results


# Todo: inplement properly
def main():
    global DISPLAY_SURFACE, GAME_STATE, NEW_GAME, GAMES
    wait_for_start(DISPLAY_SURFACE)         # slide 1
    
    round_over = False
    game_over = False
    while not game_over:  # a game
        reset_round()  # reset GAME_STATE
        char_fade(DISPLAY_SURFACE)          # slide 2 - animation
        # slide 2 - choice:
        GAME_STATE["even_mode"] = char_pick(DISPLAY_SURFACE) 
        char_chosen(DISPLAY_SURFACE)        # slide 2 - chosen animation

        while not round_over:  # a round
            numbers_load(DISPLAY_SURFACE)   # slide 3
            round_over = evaluate()         # slide 3 - anyone 6 points?
        
            round_result(DISPLAY_SURFACE)   # slide 4 - print
            GAME_STATE["round"] += 1        # slide 4

        save_winners()
        round_results(DISPLAY_SURFACE)      # slide 5
        # game over? - choice:
        game_over = not play_again(DISPLAY_SURFACE)
        round_over = False

    for line in GAMES:
        print(line)

    check_for_quit()

if __name__ == '__main__':
    main()
