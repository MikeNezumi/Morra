import sys, random, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'helpers' folder
    from helpers.globals import *
    from helpers.window import loop_footer
else:
    pass

""" INITIAL SCREEN """

def wait_for_start(surface): # initial screen animation
    global WINDOW_WIDTH, WINDOW_HEIGHT, FPS_CLOCK, FPS, FONTS, YELLOW

    t_width = 1000
    background = pygame.transform.smoothscale(pygame.image.load("graphics/title/init-bg.jpg"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    title_frame = pygame.transform.smoothscale(pygame.image.load("graphics/title/init-frame.png"), (t_width, WINDOW_HEIGHT))
    title_backlight = pygame.transform.smoothscale(pygame.image.load("graphics/title/init-backlight.png"), (1200, WINDOW_HEIGHT))
    title_backlight.set_alpha(120)
    continue_msg = SMALL_FONT.render("[ press any key to continue ]", True, YELLOW)
    title = TITLE_FONT.render("MORRA", True, YELLOW)
    
    tag0_y = 320
    tag_y = 320
    line_height = 30
    random_nums = [(str(random.randint(1, 2))) for _ in range(8)]
    tagline_strings = {
        tag0_y: "A", 
        tag0_y + line_height: "Different", 
        tag0_y + 2 * line_height: "Kind", 
        tag0_y + 3 * line_height: "of", 
        tag0_y + 4 * line_height: "Binary", 
        tag0_y + 5 * line_height: ">>> " + " ".join(random_nums) + "   "  # space to prevent overlapping render time
    }

    for i in range(26):  # frame move in from left
        surface.blit(background, (0, 0))
        surface.blit(title_backlight, (WINDOW_WIDTH - (t_width / 25) * i, 0))
        surface.blit(title_frame, (WINDOW_WIDTH - (t_width / 25) * i, 0))
        loop_footer()

    for i in range(20):  # title fades in
        title.set_alpha(i * 255 / 20)
        surface.blit(background, (0, 0))
        surface.blit(title_backlight, (WINDOW_WIDTH - t_width, 0))
        surface.blit(title_frame, (WINDOW_WIDTH - t_width, 0))
        surface.blit(title, (940, 175))
        loop_footer()

    line_i = 0
    i = 0
    while True:  # Text spelled out
        tagline = MID_FONT.render(tagline_strings[tag_y][:i], True, YELLOW)
        surface.blit(background, (0, 0))
        surface.blit(title_backlight, (WINDOW_WIDTH - t_width, 0))
        surface.blit(title_frame, (WINDOW_WIDTH - t_width, 0))
        surface.blit(title, (940, 175))
        surface.blit(tagline, (940, tag_y))
        for lines in range(line_i):  # retrospective printing previous lines
            tagline = MID_FONT.render(tagline_strings[tag0_y + line_height*lines], True, YELLOW)
            surface.blit(tagline, (940, tag0_y + line_height*lines))

        i += 1
        if i == len(tagline_strings[tag_y]):
            line_i += 1
            tag_y += line_height
            i = 0
        if line_i == len(tagline_strings):
            break
        loop_footer()

    # continue message flicking
    surface.blit(title, (940, 175))
    done = False
    pygame.time.wait(500)
    while not done:
        for i in range(30):
            if i == 0:
                surface.blit(continue_msg, (940, 550))
            elif i == 15:
                surface.blit(background, (0, 0))
                surface.blit(title_backlight, (WINDOW_WIDTH - t_width, 0))
                surface.blit(title, (940, 175))
                random_nums = [(str(random.randint(1, 2))) for _ in range(8)]
                tagline_strings[tag0_y + 5 * line_height] = ">>> " + " ".join(random_nums) + "   "  # space to prevent overlapping render time
                for lines in range(6):  # retrospective printing previous lines
                    tagline = MID_FONT.render(tagline_strings[tag0_y + line_height*lines], True, YELLOW)
                    surface.blit(tagline, (940, tag0_y + line_height*lines))

                surface.blit(title_frame, (WINDOW_WIDTH - t_width, 0))
            for event in pygame.event.get(pygame.KEYUP) + pygame.event.get(pygame.MOUSEBUTTONUP):
                done = True
                break
            loop_footer()