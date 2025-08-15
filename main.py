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
font_entry = pg.font.Font('fonts/InknutAntiqua-Regular.ttf', 50)
turn_font = pg.font.Font('fonts/InknutAntiqua-Regular.ttf', 40)

otn = font_start.render("Start", True, (255, 255, 255))
entry_color_inactive = pg.Color((30, 30, 30))
entry_color_active = pg.Color((0, 0, 0))
w_active = False
b_active = False
board_x, board_y = 560, 200

# Player
white_player = ''
black_player = ''
white_player_entry = pg.Rect(90, 500, 140, 70)
black_player_entry = pg.Rect(1425, 500, 140, 70)
chance = 0
dead = 0

start_button = pg.Rect(850, 750, 260, 100)
playername_font = pg.font.Font(None, 50)
playername_suface_txt = playername_font.render('Name', True, (110, 110, 111))
covering_text = playername_font.render('Name', True, (61, 61, 61))

state = 'dashboard'

# Everything Visual On The Dashboard
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

# Game Play Images Loaded
plain_bg = pg.image.load('game_img/Plain Chess Dashboard.png')
chessboard = pg.image.load('game_img/Chess_Board 800.png').convert_alpha()
trayofdead = pg.image.load('game_img/Component 3.png').convert_alpha()
promotiontray = pg.image.load('game_img/promotion_tray.png').convert_alpha()

# Chess Board
grid_size = 102

# Dict of Pieces Image
pieces_img = {
    'wk': pg.transform.scale(pg.image.load('game_img/w_pieces/w_king.png').convert_alpha(),
                             (grid_size, grid_size)),
    'wq': pg.transform.scale(pg.image.load('game_img/w_pieces/w_queen.png').convert_alpha(),
                             (grid_size, grid_size)),
    'wbr': pg.transform.scale(pg.image.load('game_img/w_pieces/w_bishop.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wbl': pg.transform.scale(pg.image.load('game_img/w_pieces/w_bishop.png').convert_alpha(),
                              (grid_size, grid_size)),
    'whr': pg.transform.scale(pg.image.load('game_img/w_pieces/w_knight.png').convert_alpha(),
                              (grid_size, grid_size)),
    'whl': pg.transform.scale(pg.image.load('game_img/w_pieces/w_knight.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wrr': pg.transform.scale(pg.image.load('game_img/w_pieces/w_rook.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wrl': pg.transform.scale(pg.image.load('game_img/w_pieces/w_rook.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wp0': pg.transform.scale(pg.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wp1': pg.transform.scale(pg.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wp2': pg.transform.scale(pg.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wp3': pg.transform.scale(pg.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wp4': pg.transform.scale(pg.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wp5': pg.transform.scale(pg.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wp6': pg.transform.scale(pg.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'wp7': pg.transform.scale(pg.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bk': pg.transform.scale(pg.image.load('game_img/b_pieces/b_king.png').convert_alpha(),
                             (grid_size, grid_size)),
    'bq': pg.transform.scale(pg.image.load('game_img/b_pieces/b_queen.png').convert_alpha(),
                             (grid_size, grid_size)),
    'bbr': pg.transform.scale(pg.image.load('game_img/b_pieces/b_bishop.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bbl': pg.transform.scale(pg.image.load('game_img/b_pieces/b_bishop.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bhr': pg.transform.scale(pg.image.load('game_img/b_pieces/b_knight.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bhl': pg.transform.scale(pg.image.load('game_img/b_pieces/b_knight.png').convert_alpha(),
                              (grid_size, grid_size)),
    'brr': pg.transform.scale(pg.image.load('game_img/b_pieces/b_rook.png').convert_alpha(),
                              (grid_size, grid_size)),
    'brl': pg.transform.scale(pg.image.load('game_img/b_pieces/b_rook.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bp0': pg.transform.scale(pg.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bp1': pg.transform.scale(pg.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bp2': pg.transform.scale(pg.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bp3': pg.transform.scale(pg.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bp4': pg.transform.scale(pg.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bp5': pg.transform.scale(pg.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bp6': pg.transform.scale(pg.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                              (grid_size, grid_size)),
    'bp7': pg.transform.scale(pg.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                              (grid_size, grid_size))
}

pieces = []
def game():
    player_w_render = font_start.render(white_player, True, (255, 255, 255))
    player_b_render = font_start.render(black_player, True, (0, 0, 0))
    turn_text = turn_font.render(f"Current Turn: {chance.capitalize()}", True, (255, 255, 255))

    screen.blit(plain_bg, (0,0))
    screen.blit(chessboard, (board_x, board_y))
    screen.blit(player_w_render, (90, 10))
    screen.blit(player_w_render, (1500, 10))
    screen.blit(turn_text, (750, 10))
    screen.blit(trayofdead, (315, 200))
    screen.blit(trayofdead, (1400, 200))

    if len(dead) != 0:
        wc = 0
        bc = 0
        for i in range(len(dead)):
            wc = 0
            bc = 0

            # Captured pieces placement calculation on the "Tray of Dead"
            for i in range(len(dead)):
                if dead[i][0] == 'w':
                    w_row = wc % 8
                    w_col = wc // 8

                    if w_col == 0:
                        wx = 435
                    else:
                        wx = 320

                    screen.blit(pieces_img[dead][i], (wx, 200 +105 * w_row))
                    wc += 1

                elif dead[i][0] == 'b':
                    b_row = bc % 8
                    b_col = bc // 8

                    if b_col == 0:
                        bx = 1405
                    else:
                        bx = 1520

                    screen.blit(pieces_img[dead[i]], (bx, 200 + 105 * b_row))
                    bc += 1
    



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

    if state == 'dashboard':
        dashboard()
        clock.tick(30)

    elif state == 'game':
        game()
        clock.tick(60)


        clock.tick(60)
    pg.display.update()