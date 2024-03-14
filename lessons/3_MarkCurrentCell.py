import pygame
from random import choice

RES = WINX, WINY = 600, 600
TILE = 100
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
THICKNESS = 2

cols = WINX // TILE
rows = WINY // TILE

class Cell:
    def __init__(self, x, y):
        # x, y coordinates
        self.x = x
        self.y = y
        self.walls = {
            'top': True,
            'bottom': True,
            'left': True,
            'right': True,
        }
        self.visited = False

    def draw(self):
        x = self.x * TILE
        y = self.y * TILE
        if self.visited:
            # rect - surface, color, (coordX, coordY, width, height)
            pygame.draw.rect(win, BLACK, (x, y, TILE, TILE))
        if self.walls['top']:
            # line - surface, color, posBEG, posEND, thickness
            pygame.draw.line(win, RED, (x, y), (x + TILE, y), THICKNESS)
        if self.walls['bottom']:
            pygame.draw.line(win, RED, (x, y + TILE), (x + TILE, y + TILE), THICKNESS)
        if self.walls['left']:
            pygame.draw.line(win, RED, (x, y), (x, y + TILE), THICKNESS)
        if self.walls['right']:
            pygame.draw.line(win, RED, (x + TILE, y), (x + TILE, y + TILE), THICKNESS)

    def draw_current_cell(self):
        x = self.x * TILE
        y = self.y * TILE
        # colour inside current cell
        pygame.draw.rect(win, GREEN, (x + THICKNESS, y + THICKNESS, TILE - THICKNESS, TILE - THICKNESS))


grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]

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

    [cell.draw() for cell in grid_cells]
    current_cell.visited = True
    current_cell.draw_current_cell()

    # refresh window
    pygame.display.flip()
    # frame rate
    clock.tick(30)