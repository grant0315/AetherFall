import pygame
import sys

import constants as c

def main():
    pygame.init()

    # Initalize Screen
    screen = pygame.display.set_mode((c.INITIAL_WINDOW_WIDTH, c.INITIAL_WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(c.WINDOW_TITLE)


if __name__ == "__main__":
    main()