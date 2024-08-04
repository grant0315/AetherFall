import pygame
import sys

import lib
import constants as c


pygame.init()

# Initalize Screen
screen = pygame.display.set_mode((c.INITIAL_WINDOW_WIDTH, c.INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(c.WINDOW_TITLE)

# Initilze Clock
clock = pygame.time.Clock()

# Initlize new sizes to avoid UnboundLocalError
new_width, new_height = c.INITIAL_WINDOW_WIDTH, c.INITIAL_WINDOW_HEIGHT


class Game:
    def __init__(self):
        self.screen = screen
        self.zoom = 1
        self.zoom_step = 0.1
        self.min_zoom = 0.5
        self.max_zoom = 2
        self.offset_x = 0
        self.offset_y = 0
        self.dragging = False
        self.last_mouse_pos = None
        self.all_sprites = pygame.sprite.Group()
        self.create_entities()

    def create_entities(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.player.move(0, 1)
                elif event.key == pygame.K_LEFT:
                    self.player.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(1, 0)
                elif event.key == pygame.K_EQUALS:
                    self.zoom = min(self.zoom + self.zoom_step, self.max_zoom)
                elif event.key == pygame.K_MINUS:
                    self.zoom = max(self.zoom - self.zoom_step, self.min_zoom)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Mouse wheel up
                    self.zoom = min(self.zoom + self.zoom_step, self.max_zoom)
                elif event.button == 5:  # Mouse wheel down
                    self.zoom = max(self.zoom - self.zoom_step, self.min_zoom)
                elif event.button == 1:  # Left mouse button down
                    self.dragging = True
                    self.last_mouse_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button up
                    self.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging:
                    mouse_x, mouse_y = event.pos
                    last_mouse_x, last_mouse_y = self.last_mouse_pos
                    self.offset_x += mouse_x - last_mouse_x
                    self.offset_y += mouse_y - last_mouse_y
                    self.last_mouse_pos = (mouse_x, mouse_y)

                    # Apply boundary conditions
                    self.apply_boundary_conditions()
        return True
    
    def apply_boundary_conditions(self):
        """Apply boundary conditions to ensure the camera does not move beyond the grid."""
        width, height = self.screen.get_size()
        max_offset_x = 0
        max_offset_y = 0
        min_offset_x = -(c.GRID_WIDTH * c.GRID_SIZE * self.zoom - width)
        min_offset_y = -(c.GRID_HEIGHT * c.GRID_SIZE * self.zoom - height)
        
        self.offset_x = max(min(self.offset_x, max_offset_x), min_offset_x)
        self.offset_y = max(min(self.offset_y, max_offset_y), min_offset_y)

    def update(self):
        for entity in self.all_sprites:
            entity.update_position(self.zoom, self.offset_x, self.offset_y)

    def draw(self):
        self.screen.fill(c.WHITE)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            # Limit frame rate
            clock.tick()
            
            running = self.handle_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.quit()
    sys.exit()
    