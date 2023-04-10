import sys, random, math, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'animations' folder
    from helpers.globals import *
    from helpers.window import loop_footer
    from helpers.misc import backlit_rect
else:
    pass

""" AT THE END OF 1 GAME, DISPLAY RESULTS (slide 5) """
def round_results(surface, static = False):
    global GAME_STATE, WINDOW_WIDTH, WINDOW_HEIGHT, BLACK_A, FPS, FONTS
    
    background = pygame.transform.smoothscale(pygame.image.load("graphics/results/results-bg.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    eavan = pygame.image.load("graphics/chars/eavan.png")    # 349 x 1000 px
    odhran = pygame.image.load("graphics/chars/odhran.png")  # 411 x 1000 px
    eavan = pygame.transform.smoothscale(eavan, (130, 400))
    odhran = pygame.transform.smoothscale(odhran, (150, 400))
    win_pics = {"Eavan": eavan, "Odhran": odhran, "neither": TITLE_FONT.render("???????", True, YELLOW)}
    frames = pygame.transform.smoothscale(pygame.image.load("graphics/results/frames.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    backlights = pygame.transform.smoothscale(pygame.image.load("graphics/results/backlights.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    backlights.set_alpha(BLACK_A)
    tag_rendered = TITLE_FONT.render("GAME HISTORY", True, YELLOW)
    (left_tag, right_tag) = ("Eavan", "Odhran") if GAME_STATE["even_mode"] else ("Odhran", "Eavan")
    lpicked = "".join([str(i) + "  " for i in GAME_STATE["picked"]])
    rpicked = "".join([str(i) + "  " for i in GAME_STATE["ai_picked"]])
    left_rendered = MID_FONT.render(left_tag, True, YELLOW)
    right_rendered = MID_FONT.render(right_tag, True, YELLOW)
    winner_rendered = MID_FONT.render("WINNER: " + GAME_STATE["winner"], True, YELLOW)
    wchar_rendered =  MID_FONT.render("(" + GAME_STATE["winner_char"] + ")", True, YELLOW)
    num_rendered = MID_FONT.render("NUMBERS CHOSEN:", True, YELLOW)
    lpicked_rendered = MID_FONT.render(lpicked, True, YELLOW)
    rpicked_rendered = MID_FONT.render(rpicked, True, YELLOW)
    lrounds_rendered = MID_FONT.render("ROUNDS WON: " + str(GAME_STATE["player_rounds"]), True, YELLOW)
    rrounds_rendered = MID_FONT.render("ROUNDS WON: " + str(GAME_STATE["ai_rounds"]), True, YELLOW)
    lpoints_rendered = MID_FONT.render("POINTS: " + str(GAME_STATE["score"]), True, YELLOW)
    rpoints_rendered = MID_FONT.render("POINTS: " + str(GAME_STATE["ai_score"]), True, YELLOW)

    init_i = 30 if static else 0
    for i in range(init_i, FPS + 11):  # descend frames
        vert_i = i if i < FPS else FPS
        surface.blit(background, (0, 0))
        surface.blit(backlights, (0, (vert_i - FPS) * 30))
        surface.blit(frames, (0, (vert_i - FPS) * 30))
        if (i >= FPS):
            a_i = round(25.5 * (i - FPS), 0)
            tag_rendered.set_alpha(a_i)
            left_rendered.set_alpha(a_i)
            right_rendered.set_alpha(a_i)
            winner_rendered.set_alpha(a_i)
            wchar_rendered.set_alpha(a_i)
            num_rendered.set_alpha(a_i)
            lrounds_rendered.set_alpha(a_i)
            lpoints_rendered.set_alpha(a_i)
            rrounds_rendered.set_alpha(a_i)
            rpoints_rendered.set_alpha(a_i)
            lpicked_rendered.set_alpha(a_i)
            rpicked_rendered.set_alpha(a_i)
            win_pics[GAME_STATE["winner_char"]].set_alpha(a_i)

            surface.blit(tag_rendered, (WINDOW_WIDTH // 2 - 157, 13))
            surface.blit(left_rendered, (190, 220))
            surface.blit(right_rendered, (WINDOW_WIDTH - 260, 220))
            surface.blit(winner_rendered, (WINDOW_WIDTH // 2 - 90, 200))
            surface.blit(wchar_rendered, (WINDOW_WIDTH // 2 - 40, 240))
            surface.blit(num_rendered, (WINDOW_WIDTH // 2 - 530, 340))
            surface.blit(win_pics[GAME_STATE["winner_char"]], (WINDOW_WIDTH // 2 - 70, 310))

            surface.blit(lrounds_rendered, (WINDOW_WIDTH // 2 - 520, 430))
            surface.blit(lpoints_rendered, (WINDOW_WIDTH // 2 - 470, 495))
            surface.blit(num_rendered, (WINDOW_WIDTH // 2 + 305, 340))
            surface.blit(lpicked_rendered, (WINDOW_WIDTH // 2 - 530, 370))

            surface.blit(rrounds_rendered, (WINDOW_WIDTH // 2 + 315, 430))
            surface.blit(rpoints_rendered, (WINDOW_WIDTH // 2 + 365, 495))
            surface.blit(rpicked_rendered, (WINDOW_WIDTH // 2 + 310, 370))

        if not static:    
            loop_footer()

def play_again(surface):  # play again? returns True / False
    global FONTS, YELLOW, BLACK_A

    chamfer = 10
    (width, height) = (320, 70)
    (lx, ly) = (220, 560)
    (rx, ry) = (750, 560)
    l_tag = TITLE_FONT.render("PLAY AGAIN?", True, YELLOW)
    r_tag = TITLE_FONT.render("FINISH GAME?", True, YELLOW)
    l_cto = SMALL_FONT.render("[ PRESS E ]", True, YELLOW)
    r_cto = SMALL_FONT.render("[ PRESS O ]", True, YELLOW)

    l_points = [
    (lx, ly), 
    (lx + width - chamfer, ly),
    (lx + width, ly + chamfer),
    (lx + width, ly + height),
    (lx + chamfer, ly + height),
    (lx, ly + height - chamfer)
    ]
    r_points = [
        (rx, ry), 
        (rx + width - chamfer, ry),
        (rx + width, ry + chamfer),
        (rx + width, ry + height),
        (rx + chamfer, ry + height),
        (rx, ry + height - chamfer)
    ]

    for i in range(5):  # flicker 'End?'
        if i % 2 == 1:
            round_results(surface, static = True)
            loop_footer()
        else:
            round_results(surface, static = True)
            backlit_rect(surface, l_points, BLACK_A, chamfer)
            backlit_rect(surface, r_points, BLACK_A, chamfer)
            surface.blit(l_tag, (lx + 20, ly  + 12))
            surface.blit(r_tag, (rx  + 15, ry  + 12))
            pygame.draw.polygon(surface, YELLOW, l_points, 5)
            pygame.draw.polygon(surface, YELLOW, r_points, 5)

            surface.blit(l_cto, (lx + 120, ly  + 80))
            surface.blit(r_cto, (rx  + 120, ry  + 80))
            loop_footer()

    continue_rect = pygame.Rect((0, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))
    while True:
        if pygame.key.get_pressed()[pygame.K_e]:
            return True
        elif pygame.key.get_pressed()[pygame.K_o]:
            return False

        for _ in pygame.event.get(pygame.MOUSEBUTTONUP):
                return continue_rect.collidepoint(pygame.mouse.get_pos())
        
        loop_footer()


def overall_results():
    pass