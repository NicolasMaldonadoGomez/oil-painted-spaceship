import pygame
from random import random

class Nave:
    """Con esta clase manejamos la nave"""

    def __init__(self, juego_invasion,):
        """inicializa la nave y establece la posicion inicial"""
        self.pantalla = juego_invasion.pantalla
        self.pantalla_rect = juego_invasion.pantalla.get_rect()
        # Creamos banderas de movimiento
        self.moviendose_derecha = False
        self.moviendose_izquierda = False
        # cargamos la imagen
        self.imagen_nave = pygame.image.load('imagenes/nave25.png')
        self.rect_nave = self.imagen_nave.get_rect()

        # la nave empieza en el centro de abajo
        self.rect_nave.midbottom = self.pantalla_rect.midbottom
        
        # cargamos la imagen del jet de fuego
        self.imagen_fuego = pygame.image.load('imagenes/jet25.png')
        self.rect_fuego   = self.imagen_fuego.get_rect()

        self.crear_propulsores(juego_invasion)

        # Traemos la configuracion de velocidad del juego
        self.velocidad = juego_invasion.configuracion.velocidad
        self.x = float(self.rect_nave.x)

    def crear_propulsores(self,juego_invasion):
        # creamos las imagenes de los propulsores derecho e izquierdo
        self.imagen_fuego_propulsor_izquierdo = pygame.transform.rotate(pygame.transform.scale(self.imagen_fuego,juego_invasion.configuracion.tamaño_propulsores),270)
        self.rect_propulsor_izquierdo = self.imagen_fuego_propulsor_izquierdo.get_rect()

        self.imagen_fuego_propulsor_derecho = pygame.transform.rotate(pygame.transform.scale(self.imagen_fuego,juego_invasion.configuracion.tamaño_propulsores),90)
        self.rect_propulsor_derecho = self.imagen_fuego_propulsor_derecho.get_rect()

        self.rect_propulsor_derecho.topright = self.rect_nave.topleft
        self.rect_propulsor_izquierdo.topright = self.rect_nave.topleft
        self.rect_propulsor_izquierdo.y += 40
        self.rect_propulsor_derecho.y += 40
    
    def actualizar_nave(self):
        if self.moviendose_derecha and self.rect_nave.x < (self.pantalla_rect.right-100):
            self.x += self.velocidad
            self.encender_propulsor_izquierdo()
        if self.moviendose_izquierda and self.rect_nave.x > 0:
            self.x -=  self.velocidad
            self.encender_propulsor_derecho()
        self.rect_nave.x = self.x
    
    def encender_propulsor_izquierdo(self):
        if random()>0.7:
            self.rect_propulsor_izquierdo.x = self.x-63
            self.pantalla.blit(self.imagen_fuego_propulsor_izquierdo, self.rect_propulsor_izquierdo)

    def encender_propulsor_derecho(self):
        if random()>0.7:
            self.rect_propulsor_derecho.x = self.x-8
            self.pantalla.blit(self.imagen_fuego_propulsor_derecho, self.rect_propulsor_derecho)

    def dibujame(self):
        self.pantalla.blit(self.imagen_nave, self.rect_nave)
        # self.pantalla.blit(self.imagen_fuego , self.rect_nave)
    
