import pygame

import constants as c

class GridEntity(pygame.sprite.Sprite):
    def __init__(self, grid_x, grid_y, color):
        super().__init__()
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.color = color
        self.image = pygame.Surface((c.GRID_SIZE, c.GRID_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.update_position(1, 0, 0)  # Initial zoom level is 1 and offset (0,0)

    def update_position(self, zoom, offset_x, offset_y):
        """Update the entity's pixel position based on its grid position, zoom level, and camera offset."""
        self.rect.topleft = grid_to_pixel(self.grid_x, self.grid_y, zoom, offset_x, offset_y)

    def move(self, dx, dy):
        """Move the entity by (dx, dy) on the grid."""
        self.grid_x += dx
        self.grid_y += dy

    @staticmethod
    def draw_grid(surface, grid_size, color, zoom, offset_x, offset_y):
        """Draw grid lines on the surface considering zoom and camera offset."""
        width, height = surface.get_size()
        start_x = -offset_x % int(grid_size * zoom)
        start_y = -offset_y % int(grid_size * zoom)
        end_x = c.GRID_WIDTH * grid_size * zoom + offset_x
        end_y = c.GRID_HEIGHT * grid_size * zoom + offset_y
        
        for x in range(start_x, width, int(grid_size * zoom)):
                print(f"xline positions: ({x + offset_x}, {0}), ({x + offset_x}, {end_y})")
                pygame.draw.line(surface, color, (x + offset_x, 0), (x + offset_x, end_y))
        for y in range(start_y, height, int(grid_size * zoom)):
                pygame.draw.line(surface, color, (0, y + offset_y), (end_x, y + offset_y))



def grid_to_pixel(grid_x, grid_y, zoom, offset_x, offset_y):
    """Convert grid coordinates to pixel coordinates considering zoom and camera offset."""
    return int(grid_x * c.GRID_SIZE * zoom) + offset_x, int(grid_y * c.GRID_SIZE * zoom) + offset_y