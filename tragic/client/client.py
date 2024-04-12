"""
This module contains a single class called Client that represents a game client
providing access to a tragic server cluster.
"""

# Standard library imports
import sys

# Third-party imports
import pygame

# Constants

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

FRAMES_PER_SECOND = 60
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Client:
    """
    This class represents a game client that provides access to a tragic server cluster.
    """
    def __init__(self):

        # Initialize PyGame
        pygame.init()
        
        display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        display_surface.fill(BLACK)

        clock = pygame.time.Clock()

        # Game loop
        while True:

            # Wait until it's time to render again
            clock.tick(FRAMES_PER_SECOND)

            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Render
            pygame.display.update()
