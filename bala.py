import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    def __init__(self,juego_invasion):
        super().__init__("")
        self.pantalla = juego_invasion.pantalla
        self.configuracion = juego_invasion.configuracion
        self.bala_color = juego_invasion.configuracion.bala_color

        #Crear una bala en 0 0 y luego mover la posicion
        self.rect = pygame.Rect(0,0,self.configuracion.bala_ancho,self.configuracion.bala_alto)
        self.rect.midtop = juego_invasion.nave.rect_nave.midtop
        self.y = float (self.rect.y)
    
    def update(self):
        self.y -= self.configuracion.bala_velocidad
        self.rect.y = self.y

    def dibujar_bala(self):
        pygame.draw.rect(self.pantalla, self.bala_color,self.rect)

