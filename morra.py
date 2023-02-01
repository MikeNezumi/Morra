import sys, math, random, pygame
from pygame.locals import *
from helpers.globals import *
from helpers.window import terminate, check_for_quit, loop_footer

""" INITIAL SCREEN """

def wait_for_start(surface): #initial screen
    global WINDOW_WIDTH, WINDOW_HEIGHT, FPS_CLOCK, FPS, BASIC_FONT

    title = pygame.transform.scale(pygame.image.load("graphics/init-frame.png"), (400, 350))
    background = pygame.transform.scale(pygame.image.load("graphics/init-bg.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    for i in range(FPS//2):
        surface.blit(background, (0, 0))
        surface.blit(title, (60, 50 - i*2))
        loop_footer()
    done = False
    pygame.time.wait(500)
    while not done:
        for i in range(25):
            if i == 0:
                surface.blit(BASIC_FONT.render(" - press any key to play - ", True, (0, 0, 0)), (110, 280))
            elif i == 12:
                surface.blit(background, (0, 0))
                surface.blit(title, (60, 22))
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
