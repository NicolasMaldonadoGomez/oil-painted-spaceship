import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, juego_invasion):
        super().__init__()
        self.pantalla = juego_invasion.pantalla

        self.image = pygame.image.load('imagenes/invaderUFO12.5.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    
    def dibuja(self):
        self.pantalla.blit(self.image, self.rect)
