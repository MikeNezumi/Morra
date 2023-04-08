import sys, random, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'helpers' folder
    from helpers.globals import *
    from helpers.window import loop_footer
    from helpers.misc import backlit_rect
else:
    pass

""" ODD/EVEN CHOICE FADE-IN """
def char_fade(surface, static = False): # Eavan and Odhran char animation
    global WINDOW_WIDTH, WINDOW_HEIGHT, FPS_CLOCK, FPS, FONTS, YELLOW, BLACK_A
    background = pygame.transform.smoothscale(pygame.image.load("graphics/title/init-bg.jpg"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    eavan = pygame.image.load("graphics/chars/eavan.png")    # 349 x 1000 px
    odhran = pygame.image.load("graphics/chars/odhran.png")  # 411 x 1000 px
    eavan = pygame.transform.smoothscale(eavan, (130, 400))
    odhran = pygame.transform.smoothscale(odhran, (150, 400))
    backlight = pygame.transform.smoothscale(pygame.image.load("graphics/chars/char-backlight.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    backlight.set_alpha(BLACK_A)
    frame_points = [
        (WINDOW_WIDTH // 2, 10), 
        (WINDOW_WIDTH // 2 - 150, 90), 
        (WINDOW_WIDTH // 2, 170),
        (WINDOW_WIDTH // 2 + 150, 90)
    ]
    title = TITLE_FONT.render("CHOOSE", True, YELLOW)
    (eavan_x, eavan_y) = (WINDOW_WIDTH // 2 - 180 - 200, 100)
    (odhran_x, odhran_y) = (WINDOW_WIDTH // 2 + 200, 100)
    even_points = [(eavan_x, 530), (eavan_x + 180, 530), (eavan_x + 180, 600), (eavan_x, 600)]
    odd_points = [(odhran_x, 530), (odhran_x + 180, 530), (odhran_x + 180, 600), (odhran_x, 600)]
    eavan_tag = MID_FONT.render("Eavan (EVEN)", True, YELLOW)
    odhran_tag = MID_FONT.render("Odhran (ODD)", True, YELLOW)

    init_frames = FPS - 1 if static else 0
    for i in range(init_frames, FPS):  # characters fade in from sides
        surface.blit(background, (0, 0))
        surface.blit(backlight, (0, 0))
        pygame.draw.polygon(surface, YELLOW, frame_points, 10)
        title.set_alpha(i * 255 / 30)
        surface.blit(title, (WINDOW_WIDTH // 2 - 87, 65))
        pygame.draw.line(surface, YELLOW, (WINDOW_WIDTH // 2 - 10, 195), (WINDOW_WIDTH // 2 - 10, 220 + 14 * i), 2)
        pygame.draw.line(surface, YELLOW, (WINDOW_WIDTH // 2, 210), (WINDOW_WIDTH // 2, 220 + 15 * i), 2)
        pygame.draw.line(surface, YELLOW, (WINDOW_WIDTH // 2 + 10, 195), (WINDOW_WIDTH // 2 + 10, 220 + 14 * i), 2)
        surface.blit(eavan, (eavan_x - 12 * (FPS - i), eavan_y))
        surface.blit(odhran, (odhran_x + 12 * (FPS - i), odhran_y))
        backlit_rect(surface, even_points, BLACK_A)
        backlit_rect(surface, odd_points, BLACK_A)
        pygame.draw.polygon(surface, YELLOW, even_points, 3)
        pygame.draw.polygon(surface, YELLOW, odd_points, 3)
        surface.blit(eavan_tag, (eavan_x + 15, 550))
        surface.blit(odhran_tag, (odhran_x + 15, 550))         
        loop_footer()

""" PLAYER MAKES ODD/EVEN CHOICE """
def char_pick(surface):  # True -> even, False -> odd
    eavan_cto = MID_FONT.render("[ press E ]", True, YELLOW)
    odhran_cto = MID_FONT.render("[ press O ]", True, YELLOW) 
    while True:
        for i in range (FPS):
            if i == 0:
                char_fade(surface, static = True)
            elif i == FPS // 2:
                surface.blit(eavan_cto, (295, 620))
                surface.blit(odhran_cto, (875, 620))

            if pygame.key.get_pressed()[pygame.K_e]:
                return True
            elif pygame.key.get_pressed()[pygame.K_o]:
                return False
            
            loop_footer()

def char_chosen(surface):
    global GAME_STATE

    if GAME_STATE["even_mode"]:
        pass
    else:
        pass