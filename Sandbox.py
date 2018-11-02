# Script to be used to test new implementations without breaking the game

import pygame
import random

#
WIDTH = 1024
HEIGHT = 768
FPS = 30

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()


#Game Loop
running = True

# -------- Main Program Loop -----------
while running:
    # keep the loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()

    # Draw / render
        # background image
    screen.fill(BLACK)

    all_sprites.draw(screen)

        #drawing code should go here

        # *after* drawing everything, flip the display (double buffering concept)
    pygame.display.flip()

# Close the window and quit.
pygame.quit()