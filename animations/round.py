import sys, random, math, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'animations' folder
    from helpers.globals import *
    from helpers.window import loop_footer
    from helpers.misc import keyboard, backlit_rect
else:
    pass

"DROPS IN A KEYBOARD OF CLICK-RESPONSIVE 1-10 KEYS, REUTRNS RECTS IF STATIC"
def keys_drop(surface, static = False):
    global WINDOW_WIDTH, WINDOW_HEIGHT, GAME_STATE, TITLE_FONT, YELLOW, BLACK_A

    background = pygame.transform.smoothscale(pygame.image.load("graphics/title/init-bg.jpg"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    eavan = pygame.image.load("graphics/chars/eavan.png")    # 349 x 1000 px
    odhran = pygame.image.load("graphics/chars/odhran.png")  # 411 x 1000 px
    eavan = pygame.transform.smoothscale(eavan, (130, 400))
    odhran = pygame.transform.smoothscale(odhran, (150, 400))
    avatars = {True: eavan, False: odhran}
    keys = [
        [str(i) for i in range(1, 11)], 
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
    ]
    side, margin, chamfer = 70, 20, 10
    left_margin = (WINDOW_WIDTH - len(keys[0]) * (side + margin)) // 2
    frame_tag = "ROUND " + str(GAME_STATE["round"])
    frame = pygame.image.load("graphics/round/trapezoid.png")
    frame_backlight = pygame.image.load("graphics/round/trap_backlight.png")
    frame = pygame.transform.smoothscale(frame, (WINDOW_WIDTH, WINDOW_HEIGHT))
    frame_backlight = pygame.transform.smoothscale(frame_backlight, (WINDOW_WIDTH, WINDOW_HEIGHT))
    frame_backlight.set_alpha(BLACK_A)
    tag_rendered = TITLE_FONT.render(frame_tag, True, YELLOW)

    init_frames = 20 if static else 0
    for i in range(init_frames, 21):  # quick (dead) keyboard drop-in animation
        pix_i = i if i < 11 else 10
        frame_xy = (0, -200 + 20 * pix_i)

        surface.blit(background, (0, 0))
        surface.blit(avatars[GAME_STATE["even_mode"]], (40, 320))
        surface.blit(avatars[not GAME_STATE["even_mode"]], (1100, 320))
        tag_a = 0 if i < 11 else 25 * (i - 10)
        tag_rendered.set_alpha(tag_a)
        surface.blit(frame_backlight, frame_xy)
        surface.blit(frame, frame_xy)
        surface.blit(tag_rendered, (WINDOW_WIDTH // 2 - 90, 27))

        if not static:
            keyboard(surface, keys, (left_margin, - 200 + 32*pix_i), side, margin, chamfer)
            loop_footer()
        else:
            return keyboard(surface, keys, (left_margin, - 200 + 32*pix_i), side, margin, chamfer)
        
        
" DROPS KEYS, SHOWS TARGET NUMBER, WAITS FOR USER INPUT 1 - 10"
def numbers_load(surface):
    global WINDOW_WIDTH, YELLOW, BLACK_A, FONTS, GAME_STATE

    chamfer = 20
    t_points = [
        (WINDOW_WIDTH // 2 - 120, 350),
        (WINDOW_WIDTH // 2 + 120 - chamfer, 350),
        (WINDOW_WIDTH // 2 + 120, 350 + chamfer),
        (WINDOW_WIDTH // 2 + 120, 600),
        (WINDOW_WIDTH // 2 - 120 + chamfer, 600),
        (WINDOW_WIDTH // 2 - 120, 600 - chamfer)
    ]
    target_line = "Target number  "
    
    keys_drop(surface)
    keys = keys_drop(surface, static = True)
    for ch_i in range(1, len(target_line) + 1):  # spell out target line
        line = MID_FONT.render(target_line[:ch_i], True, YELLOW)

        keys_drop(surface, static = True)
        backlit_rect(surface, t_points, BLACK_A, chamfer)
        pygame.draw.polygon(surface, YELLOW, t_points, 10)
        surface.blit(line, (560, 380))
        loop_footer()

    GAME_STATE["target"] = random.randint(2, 21)
    GAME_STATE["ai_picked"] = random.randint(1, 11)
    for i in range(8):  # number selection load
        num = chr(random.randint(33, 65)) if i < (8 - 1) else str(GAME_STATE["target"])
        num_rendered = MEGA_FONT.render(num, True, YELLOW)

        keys_drop(surface, static = True)
        backlit_rect(surface, t_points, BLACK_A, chamfer)
        pygame.draw.polygon(surface, YELLOW, t_points, 10)
        surface.blit(line, (560, 380))
        surface.blit(num_rendered, (WINDOW_WIDTH // 2 - 20, 450))
        loop_footer()

    num_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                 pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]
    let_keys = [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t,
                 pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p]
    letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
    GAME_STATE["picked"] = None
    while GAME_STATE["picked"] == None:  # waiting for player choice 1 - 10
        for i in range(10):
            if pygame.key.get_pressed()[num_keys[i]] \
            or pygame.key.get_pressed()[let_keys[i]]:
                GAME_STATE["picked"] = i + 1
                break
            
            for key_row in keys:
                if key_row[i].collidepoint(pygame.mouse.get_pos())  \
                and len(pygame.event.get(pygame.MOUSEBUTTONUP)) > 0:
                    GAME_STATE["picked"] = i + 1
                    break
        
        loop_footer()
    
    # Flash chosen key to signal number
    side, margin = 70, 20
    left_margin = (WINDOW_WIDTH - len(keys[0]) * (side + margin)) // 2
    num_xy = (left_margin + (side + margin) * (GAME_STATE["picked"] - 1), 125)
    let_xy = (left_margin + (side + margin) * (GAME_STATE["picked"] - 1), 125 + (side + margin))
    for i in range(10):
        if 2 < i < 9:  # draws a 1-key 'keyboard' over scene to simulate click
            keyboard(surface, [[str(GAME_STATE["picked"])]], num_xy, side, margin, chamfer = 10)
            keyboard(surface, [[letters[GAME_STATE["picked"] - 1]]], let_xy, side, margin, chamfer = 10)
        elif i == 9:
            keys_drop(surface, static = True)
            backlit_rect(surface, t_points, BLACK_A, chamfer)
            pygame.draw.polygon(surface, YELLOW, t_points, 10)
            surface.blit(line, (560, 380))
            surface.blit(num_rendered, (WINDOW_WIDTH // 2 - 20, 450))
        
        loop_footer()
