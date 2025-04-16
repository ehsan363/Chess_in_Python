import pygame
import sys
import valid as main

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
run = True
pygame.display.set_caption('Python Chess')
clock = pygame.time.Clock()

dashboard_img = pygame.image.load('interface_img/Chess Dashboard.png')
logo = pygame.image.load('interface_img/Chess by Python logo.png')
pygame.display.set_icon(logo)

font_start = pygame.font.Font('fonts/InknutAntiqua-Regular.ttf', 70)
otn = font_start.render("Start", True, (255, 255, 255))

font_entry = pygame.font.Font('fonts/InknutAntiqua-Regular.ttf', 50)
entry_color_inactive = pygame.Color((139, 78, 57))
entry_color_active = pygame.Color((103, 37, 14))
color = entry_color_inactive
w_active = False
b_active = False
white_player = ''
black_player = ''
white_player_entry = pygame.Rect(90, 500, 140, 70)
black_player_entry = pygame.Rect(1425, 500, 140, 70)

start_button = pygame.Rect(850, 750, 260, 100)
playername_font = pygame.font.Font(None, 50)
playername_suface_txt = playername_font.render('Name', True, (110, 110, 111))
covering_text = playername_font.render('Name', True, (220, 220, 220))


grid_size = 102
rows, cols = 8, 8
valid_pos = [(x, y) for x in range(cols) for y in range(rows)]
chance = 'white'

board_x, board_y = 560, 200

def grid_to_pixel(pos):
    return board_x + pos[0] * grid_size, board_y + pos[1] * grid_size

def pixel_to_grid(pos):
    x = (pos[0] - board_x) // grid_size
    y = (pos[1] - board_y) // grid_size


    if 0 <= x < 8 and 0 <= y < 8:
        return x, y
    return None


pieces_img = {
    'w_king': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_king.png').convert_alpha(),(grid_size, grid_size)),
    'w_queen': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_queen.png').convert_alpha(),(grid_size, grid_size)),
    'wr_bishop': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_bishop.png').convert_alpha(),(grid_size, grid_size)),
    'wl_bishop': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_bishop.png').convert_alpha(),(grid_size, grid_size)),
    'wr_horse': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_knight.png').convert_alpha(),(grid_size, grid_size)),
    'wl_horse': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_knight.png').convert_alpha(),(grid_size, grid_size)),
    'wr_rook': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_rook.png').convert_alpha(),(grid_size, grid_size)),
    'wl_rook': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_rook.png').convert_alpha(),(grid_size, grid_size)),
    'w1_pawn': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'w2_pawn': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'w3_pawn': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'w4_pawn': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'w5_pawn': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'w6_pawn': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'w7_pawn': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'w8_pawn': pygame.transform.scale(pygame.image.load('game_img/w_pieces/w_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'b_king': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_king.png').convert_alpha(),(grid_size, grid_size)),
    'b_queen': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_queen.png').convert_alpha(),(grid_size, grid_size)),
    'br_bishop': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_bishop.png').convert_alpha(),(grid_size, grid_size)),
    'bl_bishop': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_bishop.png').convert_alpha(),(grid_size, grid_size)),
    'br_horse': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_knight.png').convert_alpha(),(grid_size, grid_size)),
    'bl_horse': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_knight.png').convert_alpha(),(grid_size, grid_size)),
    'br_rook': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_rook.png').convert_alpha(),(grid_size, grid_size)),
    'bl_rook': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_rook.png').convert_alpha(),(grid_size, grid_size)),
    'b1_pawn': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'b2_pawn': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'b3_pawn': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'b4_pawn': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'b5_pawn': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'b6_pawn': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'b7_pawn': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),(grid_size, grid_size)),
    'b8_pawn': pygame.transform.scale(pygame.image.load('game_img/b_pieces/b_pawn.png').convert_alpha(),(grid_size, grid_size))
}

white_piece = [
    ['rook_l', (0, 0)], ['horse_l', (1, 0)], ['bishop_l', (2, 0)], ['queen', (3, 0)],
    ['king', (4, 0)], ['bishop_r', (5, 0)], ['horse_r', (6, 0)], ['rook_r', (7, 0)],
    ['pawn_1', (0, 1)], ['pawn_2', (1, 1)], ['pawn_3', (2, 1)], ['pawn_4', (3, 1)],
    ['pawn_5', (4, 1)], ['pawn_6', (5, 1)], ['pawn_7', (6, 1)], ['pawn_8', (7, 1)]
]

black_piece = [
    ['rook_l', (0, 7)], ['horse_l', (1, 7)], ['bishop_l', (2, 7)], ['queen', (3, 7)],
    ['king', (4, 7)], ['bishop_r', (5, 7)], ['horse_r', (6, 7)], ['rook_r', (7, 7)],
    ['pawn_1', (0, 6)], ['pawn_2', (1, 6)], ['pawn_3', (2, 6)], ['pawn_4', (3, 6)],
    ['pawn_5', (4, 6)], ['pawn_6', (5, 6)], ['pawn_7', (6, 6)], ['pawn_8', (7, 6)]
]


state = 'dashboard'
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


def gameplay(w_player, b_player):
    screen.blit(plain_bg, (0, 0))
    screen.blit(chessboard, (board_x, board_y))

    playername_font = pygame.font.Font('fonts/InknutAntiqua-Regular.ttf', 70)
    player_w_render = playername_font.render(w_player, True, (255, 255, 255))
    player_b_render = playername_font.render(b_player, True, (0, 0, 0))

    screen.blit(player_w_render, (90, 10))
    screen.blit(player_b_render, (1500, 10))
    screen.blit(trayofdead, (315, 200))
    screen.blit(trayofdead, (1400, 200))


def state_changer():
    global state
    state = 'game'

class Piece:
    def __init__(self, position, image_path):
        self.pos = position
        self.image_path = image_path
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def draw(self):
        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            draw_x = mouse_x - self.offset_x
            draw_y = mouse_y - self.offset_y
            screen.blit(self.image_path, (draw_x, draw_y))
        else:
            px, py = grid_to_pixel(self.pos)
            screen.blit(self.image_path, (px, py))

    def handle_mouse_down(self, mouse_pos):
        px, py = grid_to_pixel(self.pos)
        rect = pygame.Rect(px, py, grid_size, grid_size)
        if rect.collidepoint(mouse_pos):
            self.dragging = True
            self.offset_x = mouse_pos[0] - px
            self.offset_y = mouse_pos[1] - py
            return True
        return False

    def handle_mouse_up(self):
        self.dragging = False
        new_grid_pos = pixel_to_grid(pygame.mouse.get_pos())

        if new_grid_pos is None:
            return

        for i in range(len(white_piece)):
            if self.pos == white_piece[i][1]:
                if new_grid_pos in valid_pos:
                    white_piece[i][1] = new_grid_pos
                    self.pos = new_grid_pos
                    return

        for i in range(len(black_piece)):
            if self.pos == black_piece[i][1]:
                if new_grid_pos in valid_pos:
                    black_piece[i][1] = new_grid_pos
                    self.pos = new_grid_pos
                    return
        main.change_changer(chance)

pieces = [
    Piece((0, 0), pieces_img["wl_rook"]),
    Piece((1, 0), pieces_img["wl_horse"]),
    Piece((2, 0), pieces_img["wl_bishop"]),
    Piece((3, 0), pieces_img["w_queen"]),
    Piece((4, 0), pieces_img["w_king"]),
    Piece((5, 0), pieces_img["wr_bishop"]),
    Piece((6, 0), pieces_img["wr_horse"]),
    Piece((7, 0), pieces_img["wr_rook"]),
    Piece((0, 1), pieces_img["w1_pawn"]),
    Piece((1, 1), pieces_img["w2_pawn"]),
    Piece((2, 1), pieces_img["w3_pawn"]),
    Piece((3, 1), pieces_img["w4_pawn"]),
    Piece((4, 1), pieces_img["w5_pawn"]),
    Piece((5, 1), pieces_img["w6_pawn"]),
    Piece((6, 1), pieces_img["w7_pawn"]),
    Piece((7, 1), pieces_img["w8_pawn"]),
    Piece((0, 7), pieces_img["bl_rook"]),
    Piece((1, 7), pieces_img["bl_horse"]),
    Piece((2, 7), pieces_img["bl_bishop"]),
    Piece((3, 7), pieces_img["b_queen"]),
    Piece((4, 7), pieces_img["b_king"]),
    Piece((5, 7), pieces_img["br_bishop"]),
    Piece((6, 7), pieces_img["br_horse"]),
    Piece((7, 7), pieces_img["br_rook"]),
    Piece((0, 6), pieces_img["b1_pawn"]),
    Piece((1, 6), pieces_img["b2_pawn"]),
    Piece((2, 6), pieces_img["b3_pawn"]),
    Piece((3, 6), pieces_img["b4_pawn"]),
    Piece((4, 6), pieces_img["b5_pawn"]),
    Piece((5, 6), pieces_img["b6_pawn"]),
    Piece((6, 6), pieces_img["b7_pawn"]),
    Piece((7, 6), pieces_img["b8_pawn"])
]

cc = 0

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                for piece in reversed(pieces):
                    if piece.handle_mouse_down(event.pos):
                        pieces.remove(piece)
                        pieces.append(piece)
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                for piece in pieces:
                    if piece.dragging:
                        piece.handle_mouse_up()

    if state == 'dashboard':
        dashboard()
    elif state == 'game':
        if cc == 0:
            cc += 1
            print('White:', white_player)
            print('Black:', black_player)

        gameplay(white_player, black_player)

        for piece in pieces:
            piece.draw()

    pygame.display.update()
    clock.tick(60)
