import sys, math, random, pygame
from pygame.locals import *
from helpers.globals import *
from helpers.window import terminate, check_for_quit, loop_footer

""" INITIAL SCREEN """

def wait_for_start(surface): # initial screen
    global WINDOW_WIDTH, WINDOW_HEIGHT, FPS_CLOCK, FPS, BASIC_FONT

    t_width = 1000
    title_frame = pygame.transform.scale(pygame.image.load("graphics/init-frame.png"), (t_width, WINDOW_HEIGHT))
    background = pygame.transform.scale(pygame.image.load("graphics/init-bg.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    continue_msg = TITLE_FONT.render("[ press any key to continue ]", True, (237, 239, 0))
    title = NAME_FONT.render("MORRA", True, (237, 239, 0))

    for i in range(26):
        surface.blit(background, (0, 0))
        surface.blit(title_frame, (WINDOW_WIDTH - (t_width / 25) * i, 0)
        loop_footer()

    surface.blit(title, (940, 170))
    done = False
    pygame.time.wait(500)
    while not done:
        for i in range(30):
            if i == 0:
                surface.blit(continue_msg, (970, 570))
            elif i == 15:
                surface.blit(background, (0, 0))
                surface.blit(title, (940, 170))
                surface.blit(title_frame, (WINDOW_WIDTH - 1000, 0))
            for event in pygame.event.get(pygame.KEYUP):
                done = True
                break
            loop_footer()

# Todo: inplement properly
def main():
    global DISPLAY_SURFACE
    wait_for_start(DISPLAY_SURFACE)
    check_for_quit()

if __name__ == '__main__':
    main()
