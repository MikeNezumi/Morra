import pygame
from pygame.locals import *
from helpers.globals import *
from helpers.window import loop_footer

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

""" DISPLAYS FRAME WITH TARGET NUMBER """
def num_frame(surface, glyph, line = "Target number "):
    global BLACK_A, YELLOW, WINDOW_WIDTH, FONTS
    
    chamfer = 20
    t_points = [
        (WINDOW_WIDTH // 2 - 120, 350),
        (WINDOW_WIDTH // 2 + 120 - chamfer, 350),
        (WINDOW_WIDTH // 2 + 120, 350 + chamfer),
        (WINDOW_WIDTH // 2 + 120, 600),
        (WINDOW_WIDTH // 2 - 120 + chamfer, 600),
        (WINDOW_WIDTH // 2 - 120, 600 - chamfer)
    ]

    glyph_rendered = MEGA_FONT.render(glyph, True, YELLOW)
    line_rendered = MID_FONT.render(line, True, YELLOW)
    backlit_rect(surface, t_points, BLACK_A, chamfer)
    pygame.draw.polygon(surface, YELLOW, t_points, 10)
    surface.blit(line_rendered, (560, 380))
    surface.blit(glyph_rendered, (WINDOW_WIDTH // 2 - 20, 450))

""" SHOWS A PLAYER STAT IN AN ARBITRARILY POSITIONED FRAME"""
def player_frame(surface, topleft, player = True):  # stop_xy -> topleft corner
    global GAME_STATE, YELLOW, FONTS, BLACK_A

    height, width, chamfer = 300, 200, 20
    f_points = [
        topleft,
        (topleft[0] + width - chamfer, topleft[1]),
        (topleft[0] + width, topleft[1] + chamfer),
        (topleft[0] + width, topleft[1] + height),
        (topleft[0] + chamfer, topleft[1] + height),
        (topleft[0], topleft[1] + height - chamfer)
    ]
    is_player = {True: "score", False: "ai_score"}
    points = {True: "picked", False: "ai_picked"}
    tags = {True: "Eavan", False: "Odhran"}
    tag = tags[GAME_STATE["even_mode"]] if player else tags[not GAME_STATE["even_mode"]]
    tag_rendered = TITLE_FONT.render(tag, True, YELLOW)
    num_rendered = MEGA_FONT.render(str(GAME_STATE[points[player]]), True, YELLOW)
    points_rendered = MID_FONT.render(str(GAME_STATE[is_player[player]]) + " points", True, YELLOW)
    tag_x = 40 if tag == "Eavan" else 30
    num_x = width // 2 - 10 if GAME_STATE[points[player]] != 10 else width // 2 - 20
    
    backlit_rect(surface, f_points, BLACK_A, chamfer = chamfer)
    pygame.draw.polygon(surface, YELLOW, f_points, 10)
    surface.blit(tag_rendered, (topleft[0] + tag_x, topleft[1] + 20))
    surface.blit(num_rendered, (topleft[0] + num_x, topleft[1] + 100))
    surface.blit(points_rendered, (topleft[0] + 60, topleft[1] + 220))


