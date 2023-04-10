import pygame
from pygame.locals import *
from helpers.globals import *

""" alter GAME_STATE after 1 round """
def evaluate():  # does GAME_STATE accounting, returns True if game finished, False if not
    global GAME_STATE

    GAME_STATE["even_round"] = (GAME_STATE["picked"][-1] + GAME_STATE["ai_picked"][-1]) % 2 == 0
    
    # accounting for round winner points:
    if GAME_STATE["even_round"] == GAME_STATE["even_mode"]:
        GAME_STATE["score"] += 2
        GAME_STATE["player_rounds"] += 1
    else:
        GAME_STATE["ai_score"] += 2
        GAME_STATE["ai_rounds"] += 1

    # accounting for 'closer to target' points:  (same distance -> no points)
    player_delta = abs(GAME_STATE["picked"][-1] - GAME_STATE["target"])
    ai_delta = abs(GAME_STATE["ai_picked"][-1] - GAME_STATE["target"])
    if player_delta < ai_delta:
        GAME_STATE["score"] += 1
    elif player_delta > ai_delta:
        GAME_STATE["ai_score"] += 1

    return GAME_STATE["score"] >= 6 or GAME_STATE["ai_score"] >= 6

""" save winners into GAME_STATE after 1 game """
def save_winners():
    global GAME_STATE

    winners = {True: "You", False: "Computer"}
    chars = {True: "Eavan", False: "Odhran"}
    if GAME_STATE["score"] == GAME_STATE["ai_score"]:
        winner = "Tie!"
        winner_char = "neither"
    else:
        human_won = (GAME_STATE["score"] >= 6)
        winner = winners[human_won]
        even_won = (GAME_STATE["even_mode"] == human_won)  # True if human even wins, or odd human loses
        winner_char = chars[even_won]

    (GAME_STATE["winner"], GAME_STATE["winner_char"]) = (winner, winner_char)

def reset_round():
    global GAME_STATE, NEW_GAME

    for key in list(GAME_STATE.keys()):
        GAME_STATE[key] = NEW_GAME[key]
    
    GAME_STATE["picked"] = array('i', [])
    GAME_STATE["ai_picked"] = array('i', [])