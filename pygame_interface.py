import pygame

pygame.init()
screen = pygame.display.set_mode((1920,1080))
run = True
pygame.display.set_caption('Python Chess')
clock = pygame.time.Clock()

dashboard_img = pygame.image.load('interface_img/Chess Dashboard.png')
logo = pygame.image.load('interface_img/Chess by Python logo.png')
pygame.display.set_icon(logo)

font_start = pygame.font.Font(None, 40)
otn = font_start.render("Start", True, (255, 255, 255))

font_entry = pygame.font.Font(None,36)
entry_color_inactive = pygame.Color((139, 78, 57))
entry_color_active = pygame.Color((103,37,14))
color = entry_color_inactive
w_active = False
b_active = False
white_player = ''
black_player = ''
black_player_entry = pygame.Rect(100, 100, 140, 40)
white_player_entry = pygame.Rect(100, 100, 140, 40)

start_button = pygame.Rect(850,750,220,60)


def game_start(p1,p2):
    players = [p1,p2]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print('Player quit window')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                game_start('Player 1','Player 2')
            if white_player_entry.collidepoint(event.pos):
                w_active = not w_active
            if black_player_entry.collidepoint(event.pos):
                b_active = not b_active
            else:
                w_active = False
                b_active = False
            color = entry_color_active if w_active else entry_color_inactive
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


    screen.blit(dashboard_img,(0,0))
    pygame.draw.rect(screen,'GREEN',start_button,border_radius=15)
    screen.blit(otn, (start_button.x + 75, start_button.y + 15))
    w_txt_surface = font_entry.render(white_player, True, color)
    b_txt_surface = font_entry.render(black_player, True, color)

    width = max(200, w_txt_surface.get_width()+10)
    width = max(200, b_txt_surface.get_width()+10)
    white_player_entry.w = width
    black_player_entry.w = width

    screen.blit(w_txt_surface, (white_player_entry.x+50, white_player_entry.y+5))
    screen.blit(b_txt_surface, (black_player_entry.x+5, black_player_entry.y+50))
    pygame.draw.rect(screen, color, black_player_entry, 2)
    pygame.draw.rect(screen, color, white_player_entry, 2)

    pygame.display.update()
    clock.tick(60)