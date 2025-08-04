import pygame as pg
# Window Configuration
pg.init()
screen = pg.display.set_mode((1920, 1080))
run = True
pg.display.set_caption('Python Chess')
clock = pg.time.Clock()

# Loading Images For Dashboard
dashboard_img = pg.image.load('interface_img/Chess Dashboard.png')
logo = pg.image.load('interface_img/Chess by Python logo.png')


# Font and UI related
pg.display.set_icon(logo)
font_start = pg.font.Font('fonts/InknutAntiqua-Regular.ttf', 70)
otn = font_start.render("Start", True, (255, 255, 255))

font_entry = pg.font.Font('fonts/InknutAntiqua-Regular.ttf', 50)
entry_color_inactive = pg.Color((30, 30, 30))
entry_color_active = pg.Color((0, 0, 0))
w_active = False
b_active = False

# Player
white_player = ''
black_player = ''
white_player_entry = pg.Rect(90, 500, 140, 70)
black_player_entry = pg.Rect(1425, 500, 140, 70)

start_button = pg.Rect(850, 750, 260, 100)
playername_font = pg.font.Font(None, 50)
playername_suface_txt = playername_font.render('Name', True, (110, 110, 111))
covering_text = playername_font.render('Name', True, (61, 61, 61))

state = 'dashboard'

# Everything Visual In The Dashboard
def dashboard():
    screen.blit(dashboard_img, (0,0))
    pg.draw.rect(screen, 'GREEN', start_button, border_radius=15)
    screen.blit(otn, (start_button.x + 35, start_button.y - 45))
    w_txt_surface = font_entry.render(white_player, True, w_color)
    b_txt_surface = font_entry.render(black_player, True, b_color)

    if len(white_player) == 0:
        screen.blit(playername_suface_txt, (110, 520))
    elif len(white_player) != 0:
        screen.blit(covering_text, (110, 520))
    if len(black_player) == 0:
        screen.blit(playername_suface_txt, (1450, 520))
    elif len(black_player) != 0:
        screen.blit(covering_text, (1450, 520))

    white_player_entry.w = max(400, w_txt_surface.get_width() + 10)
    black_player_entry.w = max(410, b_txt_surface.get_width() + 10)

    screen.blit(w_txt_surface, (white_player_entry.x + 5, white_player_entry.y - 35))
    screen.blit(b_txt_surface, (black_player_entry.x + 5, black_player_entry.y - 35))
    pg.draw.rect(screen, w_color, white_player_entry, 5, border_radius=10)
    pg.draw.rect(screen, b_color, black_player_entry, 5, border_radius=10)

def state_changer():
    global state
    state = 'game'

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if state == 'dashboard':
            # Everything functional to the dashboard
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    if len(white_player) == 0 or (len(white_player) == 1 and white_player[0] == ' '):
                        white_player = 'Player 1'
                    if len(black_player) == 0 or (len(black_player) == 1 and black_player[0] == ' '):
                        black_player = 'player 2'
                    state_changer()

                if white_player_entry.collidepoint(event.pos):
                    w_active, b_active = True, False
                elif black_player_entry.collidepoint(event.pos):
                    b_active, w_active = True, False
                else:
                    w_active, b_active = False, False


            w_color = entry_color_active if w_active else entry_color_inactive
            b_color = entry_color_active if b_active else entry_color_inactive

            if event.type == pg.KEYDOWN:
                if w_active:
                    if event.key == pg.K_BACKSPACE:
                        white_player = white_player[:-1]
                    else:
                        white_player += event.unicode
                if b_active:
                    if event.key == pg.K_BACKSPACE:
                        black_player = black_player[:-1]
                    else:
                        black_player += event.unicode

def game():
    pass

    if state == 'dashboard':
        dashboard()
        clock.tick(30)

    elif state == 'game':
        game()
        

        clock.tick(60)
    pg.display.update()