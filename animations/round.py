import sys, random, math, pygame
from pygame.locals import *
if "." in __name__:  # filed is called by a script outside of 'animations' folder
    from helpers.globals import *
    from helpers.window import loop_footer
    from helpers.misc import keyboard, num_frame, trapezoid, player_frame
else:
    pass

"DROPS IN A KEYBOARD OF CLICK-RESPONSIVE 1-10 KEYS, REUTRNS RECTS IF STATIC"
def keys_drop(surface, static = False, reverse = False):
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
        frame_xy = (0, -200 + 20 * pix_i) if not reverse else (0, 0)

        surface.blit(background, (0, 0))
        surface.blit(avatars[GAME_STATE["even_mode"]], (40, 320))
        surface.blit(avatars[not GAME_STATE["even_mode"]], (1100, 320))
        if not reverse:
            tag_a = 0 if i < 11 else round(25.5 * (i - 10), 0)
        else:
            tag_a = 255
        tag_rendered.set_alpha(tag_a)
        surface.blit(frame_backlight, frame_xy)
        surface.blit(frame, frame_xy)
        surface.blit(tag_rendered, (WINDOW_WIDTH // 2 - 90, 27))

        if (not static) and (not reverse):
            keyboard(surface, keys, (left_margin, - 200 + 32*pix_i), side, margin, chamfer)
            loop_footer()
        elif (not static):
            keyboard(surface, keys, (left_margin, - 200 + 32*(10 - pix_i)), side, margin, chamfer)
            num_frame(surface, str(GAME_STATE["target"]))
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
        keys_drop(surface, static = True)
        num_frame(surface, "", target_line[:ch_i])
        loop_footer()

    GAME_STATE["target"] = random.randint(1, 10)
    GAME_STATE["ai_picked"].append(random.randint(1, 10))
    for i in range(8):  # number selection load
        num = chr(random.randint(33, 65)) if i < (8 - 1) else "?"
        keys_drop(surface, static = True)
        num_frame(surface, num)
        loop_footer()

    num_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                 pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]
    let_keys = [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t,
                 pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p]
    letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
    GAME_STATE["picked"].append(0)
    while GAME_STATE["picked"][-1] == 0:  # waiting for player choice 1 - 10
        for i in range(10):
            if pygame.key.get_pressed()[num_keys[i]] \
            or pygame.key.get_pressed()[let_keys[i]]:
                GAME_STATE["picked"][-1] = (i + 1)
                break
            
            for key_row in keys:
                if key_row[i].collidepoint(pygame.mouse.get_pos())  \
                and len(pygame.event.get(pygame.MOUSEBUTTONUP)) > 0:
                    GAME_STATE["picked"][-1] = (i + 1)
                    break
        
        loop_footer()
    
    # Flash chosen key to signal number
    side, margin = 70, 20
    left_margin = (WINDOW_WIDTH - len(keys[0]) * (side + margin)) // 2
    num_xy = (left_margin + (side + margin) * (GAME_STATE["picked"][-1] - 1), 125)
    let_xy = (left_margin + (side + margin) * (GAME_STATE["picked"][-1] - 1), 125 + (side + margin))
    for i in range(10):
        if 2 < i < 9:  # draws a 1-key 'keyboard' over scene to simulate click
            keyboard(surface, [[str(GAME_STATE["picked"][-1])]], num_xy, side, margin, chamfer = 10)
            keyboard(surface, [[letters[GAME_STATE["picked"][-1] - 1]]], let_xy, side, margin, chamfer = 10)
        elif i == 9:
            keys_drop(surface, static = True)
            num_frame(surface, num)
        
        loop_footer()

" SHOW ROUND RESULT, WAIT FOR CLICK TO CONTINUE "
def round_result(surface):
    global GAME_STATE

    background = pygame.transform.smoothscale(pygame.image.load("graphics/title/init-bg.jpg"), (WINDOW_WIDTH, WINDOW_HEIGHT))
    eavan = pygame.image.load("graphics/chars/eavan.png")    # 349 x 1000 px
    odhran = pygame.image.load("graphics/chars/odhran.png")  # 411 x 1000 px
    eavan = pygame.transform.smoothscale(eavan, (130, 400))
    odhran = pygame.transform.smoothscale(odhran, (150, 400))
    avatars = {True: eavan, False: odhran}
    tag = "ROUND " + str(GAME_STATE["round"])
    
    keys_drop(surface, False, reverse=True)
    
    left_y0, right_y0 = WINDOW_HEIGHT, -300
    left_y, right_y = 350, 350

    stop_y = 10
    def float_frames(i, flush_buttons = True):
        surface.blit(background, (0, 0))
        surface.blit(avatars[GAME_STATE["even_mode"]], (40, 320))
        surface.blit(avatars[not GAME_STATE["even_mode"]], (1100, 320))    
        trapezoid(surface, (0, 0), tag, tag_a = 255)
        num_frame(surface, str(GAME_STATE["target"]))
        player_frame(surface, (250, left_y0 - (i * (left_y0 - left_y)) // 10), True)
        player_frame(surface, (WINDOW_WIDTH - 450, right_y0 + (i * (right_y + 300)) // 10), False)
        if flush_buttons:
            loop_footer()

    for i in range(stop_y + 1):  # player card to level
        float_frames(i)

    done = False
    continue_msg = SMALL_FONT.render("[ press any key to continue ]", True, YELLOW)
    while not done:
        for i in range(FPS):
            if i == 0:
                surface.blit(continue_msg, (540, 290))
            elif i == 15:
                surface.blit(background, (0, 0))
                surface.blit(avatars[GAME_STATE["even_mode"]], (40, 320))
                surface.blit(avatars[not GAME_STATE["even_mode"]], (1100, 320))    
                trapezoid(surface, (0, 0), tag, tag_a = 255)
                num_frame(surface, str(GAME_STATE["target"]))
                float_frames(stop_y, flush_buttons = False)
            for _ in pygame.event.get(pygame.KEYUP) + pygame.event.get(pygame.MOUSEBUTTONUP):
                done = True
                break
            
            loop_footer()

    for i in range(stop_y, 31):  # player card past level
        float_frames(i)

            
