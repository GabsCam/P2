# Script to be used to test new implementations without breaking the game

import pygame
import random
import colorAndProperties
import Player


# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((colorAndProperties.WIDTH, colorAndProperties.HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
player = Player.newPlayer()
all_sprites.add(player)

#Game Loop
running = True

# -------- Main Program Loop -----------
while running:
    # keep the loop running at the right speed
    clock.tick(colorAndProperties.FPS)

    # Process input (events)
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()

    # Draw / render
        # background image
    screen.fill(colorAndProperties.BLACK)

    all_sprites.draw(screen)

        #drawing code should go here

        # *after* drawing everything, flip the display (double buffering concept)
    pygame.display.flip()

# Close the window and quit.
pygame.quit()