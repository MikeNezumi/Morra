import sys, random, math, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'animations' folder
    from helpers.globals import *
    from helpers.window import loop_footer
    from helpers.misc import keyboard, num_frame, trapezoid, player_frame
else:
    pass

""" AT THE END OF 1 GAME, DISPLAY RESULTS (slide 5) """
def results(surface):
    global GAME_STATE
    
    print()
    winners = {True: "YOU", False: "COMPUTER"}
    chars = {True: "Eavan", False: "Odhran"}
    if GAME_STATE["score"] == GAME_STATE["ai_score"]:
        print("It's a tie, bingus. Both got 6 points")
    else:
        human_won = (GAME_STATE["score"] >= 6)
        print("Winner: {} ({})".format(winners[human_won], chars[GAME_STATE["even_mode"]]))