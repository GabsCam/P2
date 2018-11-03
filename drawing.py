# Script to be used to test new implementations without breaking the game
# NAO EH PARTE TO PROGRAMA DE JOGO, É SOMENTE UM TEMPLATE COM EXEMPLOS DE COMO DESENHAR NA TELA

import pygame
import random


WIDTH = 1024
HEIGHT = 768
FPS = 30
PI = 3.141516


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

#Game Loop
running = True

# -------- Main Program Loop -----------
while running:
    # keep the loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update

    # Draw / render
        # background image
    screen.fill(WHITE)

    pygame.draw.line(screen, GREEN, [0,0], [100,100], 5)

    for y_offset in range(0,100,10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)

    pygame.draw.rect(screen,BLACK, [20, 20, 100, 100], 2)

    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI / 2, 2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)

    pygame.draw.polygon(screen, BLACK, [[50, 100], [180, 200], [200, 200], [180, 180], [200, 50]], 5)

    font_Calibri_25 = pygame.font.SysFont('Calibri', 25, False, False)
    text = font_Calibri_25.render("My Text", True, BLACK)
    screen.blit(text,[250, 250])

        # *after* drawing everything, flip the display (double buffering concept)
    pygame.display.flip()

# Close the window and quit.
pygame.quit()