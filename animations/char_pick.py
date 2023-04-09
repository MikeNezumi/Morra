import sys, random, math, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'animations' folder
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
        surface.blit(eavan, (eavan_x + 20 - 12 * (FPS - i), eavan_y))
        surface.blit(odhran, (odhran_x + 12 * (FPS - i), odhran_y))
        backlit_rect(surface, even_points, BLACK_A)
        backlit_rect(surface, odd_points, BLACK_A)
        pygame.draw.polygon(surface, YELLOW, even_points, 3)
        pygame.draw.polygon(surface, YELLOW, odd_points, 3)
        surface.blit(eavan_tag, (eavan_x + 15, 550))
        surface.blit(odhran_tag, (odhran_x + 15, 550))         
        if not static:  # loop_footer flushes events - a non-static function
            loop_footer()

""" PLAYER MAKES ODD/EVEN CHOICE """
def char_pick(surface):  # True -> even, False -> odd
    eavan_cto = MID_FONT.render("[ press E ]", True, YELLOW)
    odhran_cto = MID_FONT.render("[ press O ]", True, YELLOW)
    eavan_rect = pygame.Rect(0, 0, WINDOW_WIDTH // 2, WINDOW_HEIGHT)
    eavan_frame = [(260, 100), (440, 100), (440, 500), (260, 500)]
    odhran_frame = [(840, 100), (1020, 100), (1020, 500), (840, 500)]
    frames = {True: eavan_frame, False: odhran_frame}
    even = False

    while True:
        for i in range (FPS // 2):
            a = abs(175 - 500 // FPS * 2 * i)
            eavan_cto.set_alpha(a)
            odhran_cto.set_alpha(a)
            even = eavan_rect.collidepoint(pygame.mouse.get_pos())
            char_fade(surface, static = True)
            pygame.draw.polygon(surface, YELLOW, frames[even], 2)
            surface.blit(eavan_cto, (295, 620))
            surface.blit(odhran_cto, (875, 620))

            if pygame.key.get_pressed()[pygame.K_e] \
            or (even and len(pygame.event.get(pygame.MOUSEBUTTONUP)) > 0):
                return True
            elif pygame.key.get_pressed()[pygame.K_o] \
            or (not even and len(pygame.event.get(pygame.MOUSEBUTTONUP)) > 0):
                return False
           
            loop_footer()

""" TRANSITION TO FIRST ROUND OF GAME """
def char_chosen(surface):
    global GAME_STATE, WINDOW_HEIGHT, WINDOW_WIDTH, FPS
    
    background = pygame.transform.smoothscale(pygame.image.load("graphics/title/init-bg.jpg"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    eavan = pygame.image.load("graphics/chars/eavan.png")    # 349 x 1000 px
    odhran = pygame.image.load("graphics/chars/odhran.png")  # 411 x 1000 px
    eavan = pygame.transform.smoothscale(eavan, (130, 400))
    odhran = pygame.transform.smoothscale(odhran, (150, 400))
    backlight = pygame.transform.smoothscale(pygame.image.load("graphics/chars/char-backlight.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    backlight.set_alpha(BLACK_A)
    title = TITLE_FONT.render("CHOOSE", True, YELLOW)
    (eavan_x, eavan_y) = (WINDOW_WIDTH // 2 - 180 - 200, 100)
    (odhran_x, odhran_y) = (WINDOW_WIDTH // 2 + 200, 100)

    for i in range(FPS):  # characters disappear
        frame_points = [
            (WINDOW_WIDTH // 2, 10 - 10 * i), 
            (WINDOW_WIDTH // 2 - 150, 90 - 10 * i), 
            (WINDOW_WIDTH // 2, 170 - 10 * i),
            (WINDOW_WIDTH // 2 + 150, 90 - 10 * i)
        ]
        surface.blit(background, (0, 0))
        surface.blit(backlight, (0, 0 - 10 * i))
        pygame.draw.polygon(surface, YELLOW, frame_points, 10)
        surface.blit(eavan, (eavan_x + 8 - 15 * i, eavan_y))
        surface.blit(odhran, (odhran_x + 12 + 15 * i, odhran_y))
        surface.blit(title, (WINDOW_WIDTH // 2 - 87, 65 - 10 * i))
        pygame.draw.line(surface, YELLOW, (WINDOW_WIDTH // 2 - 10, 210 + 14 * i), (WINDOW_WIDTH // 2 - 10, 210 + 14 * 29), 2)
        pygame.draw.line(surface, YELLOW, (WINDOW_WIDTH // 2, 225 + 15 * i), (WINDOW_WIDTH // 2, 225 + 15 * 29), 2)
        pygame.draw.line(surface, YELLOW, (WINDOW_WIDTH // 2 + 10, 210 + 14 * i), (WINDOW_WIDTH // 2 + 10, 210 + 14 * 29), 2)
        loop_footer()

    avatars = {True: eavan, False: odhran}
    even = GAME_STATE["even_mode"]
    for i in range(FPS // 2):
        surface.blit(background, (0, 0))
        surface.blit(avatars[even], (i * 10 - 100, 320)) # left_x = 40
        surface.blit(avatars[not even], (WINDOW_WIDTH - 40 - i * 10, 320))  # right_x = 1100
        loop_footer()
        
