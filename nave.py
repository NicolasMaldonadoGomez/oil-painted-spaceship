import pygame

class Nave:
    """Con esta clase manejamos la nave"""

    def __init__(self, juego_invasion,):
        """inicializa la nave y establece la posicion inicial"""
        self.pantalla = juego_invasion.pantalla
        self.pantalla_rect = juego_invasion.pantalla.get_rect()

        # cargamos la imagen
        self.imagen_nave = pygame.image.load('imagenes/nave25.png')
        self.rect = self.imagen_nave.get_rect()

        # cargamos la imagen del jet de fuego
        self.imagen_jet = pygame.image.load('imagenes/jet25.png')
        # self.rect = self.imagen_jet.get_rect()

        # la nave empieza en el centro de abajo
        self.rect.midbottom = self.pantalla_rect.midbottom

    def blitme(self):
        self.pantalla.blit(self.imagen_nave, self.rect)
        self.pantalla.blit(self.imagen_jet , self.rect)
    
