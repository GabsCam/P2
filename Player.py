import pygame
import colorAndProperties
import math

class newPlayer(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Crio uma variável chamada image, defino o tamanho dela e atribuo uma cor
        self.image = pygame.Surface((32, 32))
        self.image.fill(colorAndProperties.GREEN)
        #self.image.set_colorkey(colorAndProperties.GREEN)

        # Crio uma variavel chamada rect que sera um retangulo que abrigara minha imagem
        self.rect = self.image.get_rect()
        self.rect.center = (colorAndProperties.WIDTH / 2, colorAndProperties.HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > colorAndProperties.WIDTH:
            self.rect.right = 0
