import pygame
from pygame.locals import *
from helpers.globals import *

" CREATES A SEMI-TRANSPARENT BLACK BACKLIGHT FOR YELLOW CHARS "
def backlit_rect(surface, points, alpha, chamfer = 0):  # from list of 4 points, creates black rect backlight
    if chamfer == 0:  # rect #TODO chamfered
        width = abs(points[1][0] - points[0][0])
        height = abs(points[2][1] - points[1][1])
        s = pygame.Surface((width, height))
    else:  # rect #TODO chamfered
        width = abs(points[1][0] + chamfer - points[0][0])
        height = abs(points[3][1] + chamfer - points[2][1])
        s = pygame.Surface((width, height))
    s.set_alpha(alpha)               
    s.fill((0,0,0))           
    surface.blit(s, points[0])

" LAYS OUT A KEYBOARD (see slide 3), RETURNS A MAP OF ITS PYGAME RECTS "
def keyboard(surface, buttons, init_xy, side = 70, margin = 20, chamfer = 10):  # prints a list of buttons next to each other,
    global YELLOW, MID_FONT

    alpha = 120
    button_rects = []
    side = 70
    # 'buttons' is a list (rows) of lists (keys), eg.:
    # buttons = [[1, 2, 3, 4, 5], [q, w, e, r, t]]
    for row_i in range(len(buttons)):
        button_rects.append([])
        for btn_i in range(len(buttons[row_i])):
            glyph = MID_FONT.render(buttons[row_i][btn_i], True, YELLOW)

            ax = init_xy[0] + btn_i * (margin + side)
            ay = init_xy[1] + row_i * (margin + side)
            btn_points = [
                (ax, ay), 
                (ax + side - chamfer, ay),
                (ax + side, ay + chamfer),
                (ax + side, ay + side),
                (ax + chamfer, ay + side),
                (ax, ay + side - chamfer)
            ]
            button_rects[row_i].append(pygame.Rect(btn_points[0], (side, side)))
            backlit_rect(surface, btn_points, alpha, chamfer)
            pygame.draw.polygon(surface, YELLOW, btn_points, 3)
            surface.blit(glyph, (
                btn_points[0][0] + side // 2 - 7, 
                btn_points[0][1] + side // 2 - 15
                ))
            
    return button_rects  # pygame rects in list of lists: [[Rect1, Rect2, ...], [Rect11, ...]]

" LOADS A TOP TRAPEZOID WITH TITLE "
def trapezoid(surface, start_xy, tag, tag_a = 255):
    global WINDOW_WIDTH, WINDOW_HEIGHT, GAME_STATE, TITLE_FONT, YELLOW, BLACK_A

    frame = pygame.image.load("graphics/round/trapezoid.png")
    frame_backlight = pygame.image.load("graphics/round/trap_backlight.png")
    frame = pygame.transform.smoothscale(frame, (WINDOW_WIDTH, WINDOW_HEIGHT))
    frame_backlight = pygame.transform.smoothscale(frame_backlight, (WINDOW_WIDTH, WINDOW_HEIGHT))
    frame_backlight.set_alpha(BLACK_A)
    tag_rendered = TITLE_FONT.render(tag, True, YELLOW)
    tag_rendered.set_alpha(tag_a)

    surface.blit(frame_backlight, start_xy)
    surface.blit(frame, start_xy)
    surface.blit(tag_rendered, (WINDOW_WIDTH // 2 - 90, 27))