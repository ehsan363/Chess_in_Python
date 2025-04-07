import pygame
pygame.init()

# Window setup
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Text Input Box")

# Fonts and colors
font = pygame.font.Font(None, 36)
input_box = pygame.Rect(100, 100, 140, 40)
color_inactive = pygame.Color((139, 78, 57))
color_active = pygame.Color((103,37,14))
color = color_inactive
active = False
text = ''

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print("Input:", text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill((30, 30, 30))
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

