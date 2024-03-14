import pygame
from random import choice

RES = WINX, WINY = 600, 600
TILE = 100
BLACK = (0, 0, 0)

cols = WINX // TILE
rows = WINY // TILE

# standard framework for pygame 
pygame.init()
win = pygame.display.set_mode(RES)
pygame.display.set_caption("Window Title")
clock = pygame.time.Clock()
run = True

while run:
    # background color
    win.fill(BLACK)
    for event in pygame.event.get():
        # close button
        if event.type == pygame.QUIT:
            run = False
    # refresh window
    pygame.display.flip()
    # frame rate
    clock.tick(30)