import pygame
from random import choice

THICKNESS = 2
RES = WINX, WINY = 600 + THICKNESS, 600 + THICKNESS
TILE = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

cols = WINX // TILE
rows = WINY // TILE

unscaled_image = pygame.image.load("Assets/images.png")
scaled_image = pygame.transform.scale(unscaled_image, ((WINX - THICKNESS)//TILE, (WINY - THICKNESS)//TILE))
# pygame.image.save(scaled_image, "Assets/scaled_image.png")

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

    def draw(self, current_cell = False):
        color = scaled_image.get_at((self.x, self.y))[:3] if 0 <= self.x < scaled_image.get_width() and 0 <= self.y < scaled_image.get_height() else (0, 0, 0)
        x = self.x * TILE
        y = self.y * TILE
        if self.visited:
            # rect - surface, color, (coordX, coordY, width, height)
            pygame.draw.rect(win, color, (x, y, TILE, TILE))
        if current_cell:
            # colour inside current cell
            pygame.draw.rect(win, GREEN, (x + THICKNESS, y + THICKNESS, TILE - THICKNESS, TILE - THICKNESS))

        if self.walls['top']:
            # line - surface, color, posBEG, posEND, thickness
            pygame.draw.line(win, RED, (x, y), (x + TILE, y), THICKNESS)
        if self.walls['bottom']:
            pygame.draw.line(win, RED, (x, y + TILE), (x + TILE, y + TILE), THICKNESS)
        if self.walls['left']:
            pygame.draw.line(win, RED, (x, y), (x, y + TILE), THICKNESS)
        if self.walls['right']:
            pygame.draw.line(win, RED, (x + TILE, y), (x + TILE, y + TILE), THICKNESS)

    def check_cell(self, x, y):
        '''
        returns CellObject(True) if coordinates are validate else False
        '''
        # 2D to 1D mapping of index of cell
        find_index = lambda x, y: x + y * cols
        # boundary checking
        if not 0 <= x <= cols - 1 or not 0 <= y <= rows - 1:
            return False
        # bool(Object) = True
        return grid_cells[find_index(x, y)]

    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)
        right = self.check_cell(self.x + 1, self.y)
        for direction in [top, bottom, left, right]:
            if direction and not direction.visited:
                neighbors.append(direction)
        return choice(neighbors) if neighbors else False

def remove_walls(current_cell, next_cell):
    dx = current_cell.x - next_cell.x
    dy = current_cell.y - next_cell.y
    if dx == 1:
        current_cell.walls['left'] = False
        next_cell.walls['right'] = False
    elif dx == -1:
        current_cell.walls['right'] = False
        next_cell.walls['left'] = False
    if dy == 1:
        current_cell.walls['top'] = False
        next_cell.walls['bottom'] = False
    elif dy == -1:
        current_cell.walls['bottom'] = False
        next_cell.walls['top'] = False

grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]
visited_cells = []
colors, color = [], 40


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

    # generate grid
    [cell.draw() for cell in grid_cells]
    current_cell.visited = True
    current_cell.draw(current_cell = True)
    # [pygame.draw.circle(win, colors[i], (cell.x * TILE + TILE // 2, cell.y * TILE + TILE // 2), TILE // 2 - THICKNESS) for i, cell in enumerate(visited_cells)]
    pygame.draw.rect(win, YELLOW, (current_cell.x * TILE + THICKNESS, current_cell.y * TILE + THICKNESS, TILE - THICKNESS, TILE - THICKNESS))

    next_cell = current_cell.check_neighbors()
    if next_cell:
        next_cell.visited = True
        remove_walls(current_cell, next_cell)
        visited_cells.append(current_cell)
        colors.append((color % 256, 10, 100))
        color += 1
        current_cell = next_cell
    elif visited_cells:
        current_cell = visited_cells.pop()
    else:
        pass

    # refresh window
    pygame.display.flip()
    # frame rate
    clock.tick(120)