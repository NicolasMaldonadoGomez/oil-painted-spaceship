import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, juego_invasion):
        super().__init__()
        # Traemos la pantalla principal del juego
        self.pantalla = juego_invasion.pantalla
        self.velocidad =juego_invasion.configuracion.alien_velocidad
        #Cargamos la imagen de la nave
        self.image = pygame.transform.scale( pygame.image.load('imagenes/invaderUFO12.5.png') ,juego_invasion.configuracion.tamaño_aliens)
        # Creamos el rectángulo
        self.rect = self.image.get_rect()
        # la ubicamos en una cuadricula en el punto 1,1 desde el 0
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.orientacion = 1
    
    def update(self):
        self.x += (self.velocidad *self.orientacion)
        self.rect.x = self.x
    
    def pinta(self):
        # Pintamos en la pantalla principal, vamos a usar pintar para blit y dibuajar para draw
        self.pantalla.blit(self.image, self.rect)
