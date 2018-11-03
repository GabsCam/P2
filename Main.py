# Script to be used to test new implementations without breaking the game

import pygame
from settings import *
import Player
import os

# set up assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player.newPlayer()
all_sprites.add(player)

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