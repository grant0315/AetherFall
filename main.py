import pygame
import sys

import constants as c

def main():
    pygame.init()

    # Initalize Screen
    screen = pygame.display.set_mode((c.INITIAL_WINDOW_WIDTH, c.INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(c.WINDOW_TITLE)

    # Initlize new sizes to avoid UnboundLocalError
    new_width, new_height = c.INITIAL_WINDOW_WIDTH, c.INITIAL_WINDOW_HEIGHT
    
    # Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # Capture new window size
                new_width, new_height = event.size
                screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

        # Fill screen with White Color
        screen.fill(c.WHITE)

        # Draw blue rect that dynamically resizes with the window
        pygame.draw.rect(screen, c.BLUE, (50, 50, new_width - 100, new_height - 100))

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()