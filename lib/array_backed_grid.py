import pygame

class ArrayBackedGrid(pygame.sprite.Sprite):
    def __init__(self, grid_x, grid_y, grid_size, cell_margin):
        self.grid = []
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.grid_size = grid_size
        self.cell_margin = cell_margin

        # Populate self.grid 
        for row in range(self.grid_x):
            self.grid.append([])
            for col in range(grid_y):
                self.grid[row].append(0) # Append a cell

    def draw_grid(self, screen):
        for row in range(self.grid_x):
            for col in range(self.grid_y):
                color = (255, 255, 255)
                if self.grid[row][col] == 1:
                    color = (0, 255, 0)
                pygame.draw.rect(screen,
                                 color,
                                 [(self.cell_margin + self.grid_size) * col + self.cell_margin,
                                  (self.cell_margin + self.cell_size) * row + self.cell_margin,
                                  self.grid_size,
                                  self.grid_size])