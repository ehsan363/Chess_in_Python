import pygame

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

state = 'dashboard'


def dashboard():
    screen.blit(dashboard_img, (0,0))
    pygame.draw.rect(screen, 'GREEN', start_button, border_radius=15)
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

    white_player_entry.w = w_width
    black_player_entry.w = b_width

    screen.blit

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if state == 'dashboard':
            w_color = entry_color_active if w_active else entry_color_inactive
            b_color = entry_color_active if b_active else entry_color_inactive

    if state == 'dashboard':
        dashboard()
        clock.tick(30)
    elif state == 'game':
        pass # <--- Game Function HERE
        clock.tick(60)
    pygame.display.update()