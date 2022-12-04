import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    def __init__(self,juego_invacion):
        super().__init__("")
        self.pantalla = juego_invacion.pantalla
        self.configuracion = juego_invacion.configuracion
        self.bala_color = juego_invacion.configuracion.bala_color

        #Crear una bala en 0 0 y luego mover la posicion
        self.rect_bala = pygame.Rect(0,0,self.configuracion.bala_ancho,self.configuracion.bala_alto)
        self.rect_bala.midtop = juego_invacion.nave.rect_nave.midtop
        self.y = float (self.rect_bala.y)
    
    def update(self):
        self.y -= self.configuracion.bala_velocidad
        self.rect_bala.y = self.y

    def dibujar_bala(self):
        pygame.draw.rect(self.pantalla, self.bala_color,self.rect_bala)

