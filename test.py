from os import WCONTINUED

import pygame
pygame.init()
screen = pygame.display.set_mode((1300,1000))
run = 1
while run==1:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = 0
pygame.quit()

def aaaa():
    WCONTINUED