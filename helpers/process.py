import pygame
from pygame.locals import *
from helpers.globals import *

def evaluate():  # does GAME_STATE accounting, returns True if game finished, False if not
    global GAME_STATE

    GAME_STATE["even_round"] = (GAME_STATE["picked"] + GAME_STATE["ai_picked"]) % 2 == 0
    
    # accounting for round winner points:
    if GAME_STATE["even_round"] == GAME_STATE["even_mode"]:
        GAME_STATE["score"] += 2
    else:
        GAME_STATE["ai_score"] += 2

    # accounting for 'closer to target' points:  (same distance -> no points)
    player_delta = abs(GAME_STATE["picked"] - GAME_STATE["target"])
    ai_delta = abs(GAME_STATE["ai_picked"] - GAME_STATE["target"])
    if player_delta < ai_delta:
        GAME_STATE["score"] += 1
    elif player_delta > ai_delta:
        GAME_STATE["ai_score"] += 1

    return GAME_STATE["score"] >= 6 or GAME_STATE["ai_score"] >= 6