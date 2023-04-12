import sys, random, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'helpers' folder
    from .globals import *
else:
    from globals import *

def terminate():
    pygame.quit()
    sys.exit()

""" CLOSING GAME FORCEFULLY """
def check_for_quit():
    for event in pygame.event.get(pygame.QUIT):
        if event.type == pygame.QUIT:
            terminate()

""" ONE FRAME (display update, quit button, clearing evets, next frame) """
def loop_footer(): # belongs at the end of most game loops
    global FPS, FPS_CLOCK

    pygame.display.update()
    check_for_quit()
    pygame.event.clear()
    FPS_CLOCK.tick(FPS)


def music():
    track = random.randint(1, 3)
    pygame.mixer.init()
    pygame.mixer.music.load("music/mysterytheme{}.ogg".format(track))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)