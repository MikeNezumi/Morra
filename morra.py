import sys, math, random, pygame
from pygame.locals import *
from helpers.globals import *
from helpers.window import terminate, check_for_quit, loop_footer
from animations.title import wait_for_start

# Todo: inplement properly
def main():
    global DISPLAY_SURFACE
    wait_for_start(DISPLAY_SURFACE)  # slide 1
    
    
    check_for_quit()

if __name__ == '__main__':
    main()
