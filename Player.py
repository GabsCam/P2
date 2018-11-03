import pygame
from settings import *


class newPlayer(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Crio uma variável chamada image, defino o tamanho dela e atribuo uma cor
        self.image = pygame.Surface((32, 32))
        self.image.fill(GREEN)
        #self.image.set_colorkey(settings.BLACK)
        self.y_speed = 5

        # Crio uma variavel chamada rect que sera um retangulo que abrigara minha imagem
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5

        if self.rect.left > WIDTH:
            self.rect.right = 0


