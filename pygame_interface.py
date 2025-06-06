import pygame
import sys
from main import *

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
run = True
pygame.display.set_caption('Python Chess')
clock = pygame.time.Clock()

dashboard_img = pygame.image.load('interface_img/Chess Dashboard.png')
logo = pygame.image.load('interface_img/Chess by Python logo.png')
pygame.display.set_icon(logo)

# Font and UI related
font_start = pygame.font.Font('fonts/InknutAntiqua-Regular.ttf', 70)
otn = font_start.render("Start", True, (255, 255, 255))

font_entry = pygame.font.Font('fonts/InknutAntiqua-Regular.ttf', 50)
entry_color_inactive = pygame.Color((30, 30, 30))
entry_color_active = pygame.Color((0, 0, 0))
w_active = False
b_active = False
white_player = ''
black_player = ''
white_player_entry = pygame.Rect(90, 500, 140, 70)
black_player_entry = pygame.Rect(1425, 500, 140, 70)

start_button = pygame.Rect(850, 750, 260, 100)
playername_font = pygame.font.Font(None, 50)
playername_suface_txt = playername_font.render('Name', True, (110, 110, 111))
covering_text = playername_font.render('Name', True, (61, 61, 61))

# Chess board
grid_size = 102
rows, cols = 8, 8
global chance
chance = 'white'
dragged_piece = None

board_x, board_y = 560, 200


def grid_to_pixel(pos):
    return board_x + pos[0] * grid_size, board_y + pos[1] * grid_size


def pixel_to_grid(pos):
    x = (pos[0] - board_x) // grid_size
    y = (pos[1] - board_y) // grid_size

    if 0 <= x < 8 and 0 <= y < 8:
        return x, y
    return None


# Piece images dict
pieces_img = {
    'wk': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_king.png').convert_alpha(),
                                 (grid_size, grid_size)),
    'wq': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_queen.png').convert_alpha(),
                                 (grid_size, grid_size)),
    'wbr': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_bishop.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wbl': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_bishop.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'whr': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_knight.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'whl': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_knight.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wrr': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_rook.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wrl': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_rook.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wp0': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wp1': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wp2': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wp3': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wp4': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wp5': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wp6': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'wp7': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bk': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_king.png').convert_alpha(),
                                 (grid_size, grid_size)),
    'bq': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_queen.png').convert_alpha(),
                                 (grid_size, grid_size)),
    'bbr': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_bishop.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bbl': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_bishop.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bhr': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_knight.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bhl': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_knight.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'brr': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_rook.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'brl': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_rook.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bp0': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bp1': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bp2': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bp3': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bp4': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bp5': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bp6': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                                  (grid_size, grid_size)),
    'bp7': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),
                                  (grid_size, grid_size))
}

state = 'dashboard'


# UI rendering functions
def dashboard():
    screen.blit(dashboard_img, (0, 0))
    pygame.draw.rect(screen, 'GREEN', start_button, border_radius=15)
    screen.blit(otn, (start_button.x + 35, start_button.y - 45))
    w_txt_surface = font_entry.render(white_player, True, w_color)
    b_txt_surface = font_entry.render(black_player, True, b_color)

    if len(white_player) == 0:
        screen.blit(playername_suface_txt, (110, 520))
    if len(black_player) == 0:
        screen.blit(playername_suface_txt, (1450, 520))
    if len(black_player) != 0:
        screen.blit(covering_text, (1450, 520))
    if len(white_player) != 0:
        screen.blit(covering_text, (100, 520))

    w_width = max(400, w_txt_surface.get_width() + 10)
    b_width = max(410, b_txt_surface.get_width() + 10)
    white_player_entry.w = w_width
    black_player_entry.w = b_width

    screen.blit(w_txt_surface, (white_player_entry.x + 5, white_player_entry.y - 35))
    screen.blit(b_txt_surface, (black_player_entry.x + 5, black_player_entry.y - 35))
    pygame.draw.rect(screen, b_color, black_player_entry, 5, border_radius=10)
    pygame.draw.rect(screen, w_color, white_player_entry, 5, border_radius=10)


plain_bg = pygame.image.load('game_img/Plain Chess Dashboard.png')
chessboard = pygame.image.load('game_img/Chess_Board 800.png').convert_alpha()
trayofdead = pygame.image.load('game_img/Component 3.png').convert_alpha()
promotiontray = pygame.image.load('game_img/promotion_tray.png').convert_alpha()


# Game mode function
def gameplay(w_player, b_player):
    global chance
    screen.blit(plain_bg, (0, 0))
    screen.blit(chessboard, (board_x, board_y))

    playername_font = pygame.font.Font('fonts/InknutAntiqua-Regular.ttf', 70)
    player_w_render = playername_font.render(w_player, True, (255, 255, 255))
    player_b_render = playername_font.render(b_player, True, (0, 0, 0))

    turn_font = pygame.font.Font('fonts/InknutAntiqua-Regular.ttf', 40)
    turn_text = turn_font.render(f"Current Turn: {chance.capitalize()}", True, (255, 255, 255))

    screen.blit(turn_text, (750, 10))
    screen.blit(player_w_render, (90, 10))
    screen.blit(player_b_render, (1500, 10))
    screen.blit(trayofdead, (315, 200))
    screen.blit(trayofdead, (1400, 200))


def state_changer():
    global state
    state = 'game'

def promotion_channel(side, i, j):
    if j == 0:
        x_cord = board_x

    elif j == 1:
        x_cord = board_x + 100

    elif j == 2:
        x_cord = board_x + 202

    elif j == 3:
        x_cord = board_x + 305

    elif j == 4:
        x_cord = board_x + 406

    elif j == 5:
        x_cord = board_x + 506

    elif j == 6:
        x_cord = board_x + 608

    elif j == 7:
        x_cord = board_x + 709

    y_cord = 100 if side == 'w' else 500

    promotion_cords = (x_cord, y_cord)
    screen.blit(promotiontray, (promotion_cords))

    if side == 'w':
        queen_rect = pygame.Rect(x_cord + 5, y_cord + 5, 100, 100)
        bishop_rect = pygame.Rect(x_cord + 5, y_cord + 105, 100, 100)
        knight_rect = pygame.Rect(x_cord + 5, y_cord + 210, 100, 100)
        rook_rect = pygame.Rect(x_cord + 5, y_cord + 315, 100, 100)

        screen.blit(pieces_img['wq'], queen_rect)
        screen.blit(pieces_img['wbl'], bishop_rect)
        screen.blit(pieces_img['whl'], knight_rect)
        screen.blit(pieces_img['wrl'], rook_rect)


    elif side == 'b':
        queen_rect = pygame.Rect(x_cord + 5, y_cord + 315, 100, 100)
        bishop_rect = pygame.Rect(x_cord + 5, y_cord + 210, 100, 100)
        knight_rect = pygame.Rect(x_cord + 5, y_cord + 105, 100, 100)
        rook_rect = pygame.Rect(x_cord + 5, y_cord + 5, 100, 100)

        screen.blit(pieces_img['bq'], queen_rect)
        screen.blit(pieces_img['bbl'], bishop_rect)
        screen.blit(pieces_img['bhl'], knight_rect)
        screen.blit(pieces_img['brl'], rook_rect)

    pygame.display.update()
    selection = True
    while selection:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                selection = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if queen_rect.collidepoint(pos):
                    selection = False
                    promotion(cord_x=j, cord_y=i, p='q')

                elif bishop_rect.collidepoint(pos):
                    selection = False
                    promotion(cord_x=j, cord_y=i, p='b')

                elif knight_rect.collidepoint(pos):
                    selection = False
                    promotion(cord_x=j, cord_y=i, p='h')

                elif rook_rect.collidepoint(pos):
                    selection = False
                    promotion(cord_x=j, cord_y=i, p='r')


dead = []


def captured(captured_piece):
    dead.append(captured_piece)


# The piece creator and handler
class Piece:
    def __init__(self, position, piece_id, image, chance):
        self.pos = position
        self.piece_id = piece_id
        self.image = image
        self.color = 'white' if piece_id[0] == 'w' else 'black'
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def draw(self):
        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            draw_x = mouse_x - self.offset_x
            draw_y = mouse_y - self.offset_y
            screen.blit(self.image, (draw_x, draw_y))
        else:
            px, py = grid_to_pixel(self.pos)
            screen.blit(self.image, (px, py))

    def handle_mouse_down(self, mouse_pos):
        global chance

        if self.color != chance:
            return False

        px, py = grid_to_pixel(self.pos)
        rect = pygame.Rect(px, py, grid_size, grid_size)
        if rect.collidepoint(mouse_pos):
            self.dragging = True
            self.offset_x = mouse_pos[0] - px
            self.offset_y = mouse_pos[1] - py
            return True
        return False

    def handle_mouse_up(self):
        global chance

        if not self.dragging:
            return

        self.dragging = False
        new_grid_pos = pixel_to_grid(pygame.mouse.get_pos())
        old_pos = self.pos

        if new_grid_pos is None:
            return
        pos = valid_pos(chance)

        valid_position = None
        for i in pos:
            if i[0] == self.piece_id:
                valid_position = i[1:]
                break

        if valid_position is None or new_grid_pos not in valid_position:
            return

        captured_piece = table[new_grid_pos[1]][new_grid_pos[0]]
        if captured_piece != '0':
            captured(captured_piece=captured_piece)

        table[old_pos[1]][old_pos[0]] = '0'
        table[new_grid_pos[1]][new_grid_pos[0]] = self.piece_id
        self.pos = new_grid_pos

        # Force an immediate update of the pieces after a capture or move
        update_pieces_from_table()

        # Force a screen redraw
        render_game_screen()

        # Promotion of piece
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] != '0':
                    if chance == 'white':
                        if table[i][j][:2] == 'wp' and i == 0:
                            promotion_channel(side='w', i=i, j=j)

                    elif chance == 'black':
                        if table[i][j][:2] == 'bp' and i == 7:
                            promotion_channel(side='b', i=i, j=j)

        chance = 'black' if chance == 'white' else 'white'


pieces = []
last_table_state = None


def has_table_changed():
    global last_table_state

    if last_table_state is None:
        last_table_state = [row[:] for row in table]
        return True

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != last_table_state[i][j]:
                last_table_state = [row[:] for row in table]
                return True

    return False


def update_pieces_from_table():
    global pieces

    pieces.clear()

    for i in range(8):
        for j in range(8):
            piece_id = table[i][j]
            if piece_id != '0':
                if piece_id[1] != 'k' and len(piece_id) != 3:
                    piece_id = piece_id[:-1]
                if piece_id in pieces_img:
                    pieces.append(Piece((j, i), piece_id, pieces_img[piece_id], chance))
                elif piece_id[len(piece_id)-1] in list('01234567'):
                    img_id = piece_id[:-1]
                    pieces.append(Piece((j, i), piece_id, pieces_img[img_id], chance))
                else:
                    print(f"Warning: Unknown piece ID '{piece_id}' at position ({j}, {i})")


def render_game_screen():
    gameplay(white_player, black_player)

    if len(dead) != 0:
        wc = 0
        bc = 0

        for i in range(len(dead)):
            if dead[i][0] == 'w':
                # Calculate row and column for white pieces
                w_row = wc % 8
                w_col = wc // 8

                if w_col == 0:
                    wx = 435
                else:
                    wx = 320

                screen.blit(pieces_img[dead[i]], (wx, 200 + 105 * w_row))
                wc += 1
            elif dead[i][0] == 'b':
                # Calculate row and column for black pieces
                b_row = bc % 8
                b_col = bc // 8

                if b_col == 0:
                    bx = 1405
                else:
                    bx = 1520

                screen.blit(pieces_img[dead[i]], (bx, 200 + 105 * b_row))
                bc += 1

    for piece in pieces:
        piece.draw()

    pygame.display.update()


update_pieces_from_table()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == 'dashboard':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    if len(white_player) == 0 or (len(white_player) == 1 and white_player[0] == ' '):
                        white_player = 'Player 1'
                    if len(black_player) == 0 or (len(black_player) == 1 and black_player[0] == ' '):
                        black_player = 'Player 2'
                    state_changer()

                if white_player_entry.collidepoint(event.pos):
                    w_active = True
                    b_active = False
                elif black_player_entry.collidepoint(event.pos):
                    b_active = True
                    w_active = False
                else:
                    w_active = False
                    b_active = False

            w_color = entry_color_active if w_active else entry_color_inactive
            b_color = entry_color_active if b_active else entry_color_inactive

            if event.type == pygame.KEYDOWN:
                if w_active:
                    if event.key == pygame.K_BACKSPACE:
                        white_player = white_player[:-1]
                    else:
                        white_player += event.unicode
                if b_active:
                    if event.key == pygame.K_BACKSPACE:
                        black_player = black_player[:-1]
                    else:
                        black_player += event.unicode

        elif state == 'game':
            if has_table_changed():
                update_pieces_from_table()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for piece in reversed(pieces):
                    if piece.handle_mouse_down(event.pos):
                        dragged_piece = piece
                        pieces.remove(piece)
                        pieces.append(piece)
                        break

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragged_piece:
                    dragged_piece.handle_mouse_up()
                    dragged_piece = None

    # Render screen based on state
    if state == 'dashboard':
        dashboard()
        clock.tick(30)

    elif state == 'game':
        render_game_screen()
        clock.tick(60)

    pygame.display.update()