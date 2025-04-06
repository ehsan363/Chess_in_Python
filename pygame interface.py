from sys import displayhook

import pygame
pygame.init()
screen = pygame.display.set_mode((1920,1080))
run = True
pygame.display.set_caption('Python Chess')
clock = pygame.time.Clock()

dashboard_img = pygame.image.load('interface_img/Chess Dashboard.png')
logo = pygame.image.load('interface_img/Chess by Python logo.png')

pygame.display.set_icon(logo)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print('Player quit window')

    screen.blit(dashboard_img,(0,0))

    pygame.display.update()
    clock.tick(60)