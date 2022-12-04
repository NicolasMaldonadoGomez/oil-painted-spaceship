import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self,juego_invasion,x,y):
        super().__init__()
        # trayendo configuracion
        self.pantalla      = juego_invasion.pantalla
        self.configuracion = juego_invasion.configuracion
        # Organizando la imagen
        tamaño_random    = randint(int(self.configuracion.estrella_tamaño*0.2),int(self.configuracion.estrella_tamaño))
        imagen           = pygame.image.load('imagenes/stars-png-23.png')
        imagen_a_esacala = pygame.transform.scale(imagen,(tamaño_random,tamaño_random))
        imagen_rotada    = pygame.transform.rotate(imagen_a_esacala,randint(0,90))        
        # Acomomdando la imagen
        self.image    = imagen_rotada
        self.rect     = self.image.get_rect()
        self.rect.x   = x + randint(0, 2 * juego_invasion.configuracion.espacio_entre_estrellas)
        self.rect.y   = y + randint(0, 2 * juego_invasion.configuracion.espacio_entre_filas_de_estrellas)
    # # creo que no se usa nunca
    # def pintame(self):
    #     self.pantalla.blit(self.image,self.rect)
