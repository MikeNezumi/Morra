import sys, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'helpers' folder
    from helpers.globals import *
    from helpers.window import terminate, check_for_quit, loop_footer
else:
    pass

""" INITIAL SCREEN """

def wait_for_start(surface): # initial screen animation
    global WINDOW_WIDTH, WINDOW_HEIGHT, FPS_CLOCK, FPS, BASIC_FONT

    t_width = 1000
    title_frame = pygame.transform.scale(pygame.image.load("graphics/init-frame.png"), (t_width, WINDOW_HEIGHT))
    background = pygame.transform.scale(pygame.image.load("graphics/init-bg.png"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    continue_msg = SMALL_FONT.render("[ press any key to continue ]", True, (237, 239, 0))
    title = TITLE_FONT.render("MORRA", True, (237, 239, 0))
    tagline_strings = {300: "A", 350: "Different", 400: "Kind", 450: "of", 500: "Binary", 550: ">>>  "}

    for i in range(26):  # frame move in from left
        surface.blit(background, (0, 0))
        surface.blit(title_frame, (WINDOW_WIDTH - (t_width / 25) * i, 0))
        loop_footer()

    for i in range(20):  # title fades in
        title.set_alpha(i * 255 / 20)
        surface.blit(background, (0, 0))
        surface.blit(title_frame, (WINDOW_WIDTH - t_width, 0))
        surface.blit(title, (940, 170))
        loop_footer()

    line_i = 0
    i = 0
    tag_y = 300
    while True:  # Text spelled out
        tagline = TITLE_FONT.render(tagline_strings[tag_y][:i], True, (237, 239, 0))
        surface.blit(background, (0, 0))
        surface.blit(title_frame, (WINDOW_WIDTH - t_width, 0))
        surface.blit(title, (940, 170))
        surface.blit(tagline, (940, tag_y))
        for lines in range(line_i):  # retrospective printing previous lines
            tagline = TITLE_FONT.render(tagline_strings[300 + 50*lines], True, (237, 239, 0))
            surface.blit(tagline, (940, 300 + 50*lines))

        i += 1
        if i == len(tagline_strings[tag_y]):
            line_i += 1
            tag_y += 50
            i = 0
        if line_i == len(tagline_strings):
            break
        loop_footer()

    # continue message flicking
    surface.blit(title, (940, 170))
    done = False
    pygame.time.wait(500)
    while not done:
        for i in range(30):
            if i == 0:
                surface.blit(continue_msg, (940, 650))
            elif i == 15:
                surface.blit(background, (0, 0))
                surface.blit(title, (940, 170))
                for lines in range(6):  # retrospective printing previous lines
                    tagline = TITLE_FONT.render(tagline_strings[300 + 50*lines], True, (237, 239, 0))
                    surface.blit(tagline, (940, 300 + 50*lines))

                surface.blit(title_frame, (WINDOW_WIDTH - 1000, 0))
            for event in pygame.event.get(pygame.KEYUP):
                done = True
                break
            loop_footer()
