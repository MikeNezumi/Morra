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
def keyboard(surface, buttons, init_xy, margin = 20, chamfer = 10):  # prints a list of buttons next to each other,
    global YELLOW, MID_FONT
    
    alpha = 120
    button_rects = []
    btn_side = 70
    # 'buttons' is a list (rows) of lists (keys), eg.:
    # buttons = [[1, 2, 3, 4, 5], [q, w, e, r, t]]
    for row_i in range(len(buttons)):
        for btn_i in range(len(buttons[row_i])):
            ax = init_xy[0] + btn_i * (margin + btn_side)
            ay = init_xy[1] + row_i * (margin + btn_side)
            btn_points = [
                (ax, ay), 
                (ax + btn_side - chamfer, ay),
                (ax + btn_side, ay + chamfer),
                (ax + btn_side, ay + btn_side),
                (ax + chamfer, ay + btn_side),
                (ax, ay + btn_side - chamfer)
            ]
            button_rects.append(pygame.Rect(btn_points[0], (btn_side, btn_side)))
            backlit_rect(surface, btn_points, alpha, chamfer)
            pygame.draw.polygon(surface, YELLOW, btn_points, 3)
            
    return button_rects