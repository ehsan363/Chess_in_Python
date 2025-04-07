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

font_entry = pygame.font.Font(None,60)
entry_color_inactive = pygame.Color((139, 78, 57))
entry_color_active = pygame.Color((103,37,14))
color = entry_color_inactive
w_active = False
b_active = False
white_player = ''
black_player = ''
white_player_entry = pygame.Rect(90, 500, 140, 70)
black_player_entry = pygame.Rect(1425, 500, 140, 70)

start_button = pygame.Rect(850,750,220,60)
playername_font = pygame.font.Font(None,50)
playername_suface_txt = playername_font.render('Name',True,(110, 110, 111))
covering_text = playername_font.render('Name',True,(220,220,220))


def game_start(p1,p2):
    players = [p1,p2]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print('Player quit window')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                print('white: ',white_player)
                print('black:',black_player)
                game_start('Player 1','Player 2')
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


    screen.blit(dashboard_img,(0,0))
    pygame.draw.rect(screen,'GREEN',start_button,border_radius=15)
    screen.blit(otn, (start_button.x + 75, start_button.y + 15))
    w_txt_surface = font_entry.render(white_player, True, w_color)
    b_txt_surface = font_entry.render(black_player, True, b_color)

    if len(white_player) == 0:
        screen.blit(playername_suface_txt, (110, 520))
    if len(black_player) == 0:
        screen.blit(playername_suface_txt, (1450, 520))
    if len(black_player) != 0:
        screen.blit(covering_text,(1450, 520))
    if len(white_player) != 0:
        screen.blit(covering_text,(100, 520))
        
    w_width = max(400, w_txt_surface.get_width() + 10)
    b_width = max(410, b_txt_surface.get_width() + 10)
    white_player_entry.w = w_width
    black_player_entry.w = b_width

    screen.blit(w_txt_surface, (white_player_entry.x+5, white_player_entry.y+5))
    screen.blit(b_txt_surface, (black_player_entry.x+5, black_player_entry.y+5))
    pygame.draw.rect(screen, b_color, black_player_entry, 5, border_radius=10)
    pygame.draw.rect(screen, w_color, white_player_entry, 5, border_radius=10)

    pygame.display.update()
    clock.tick(60)