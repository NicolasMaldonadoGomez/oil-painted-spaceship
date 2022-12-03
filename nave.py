import pygame

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
        self.rect = self.imagen_nave.get_rect()

        # cargamos la imagen del jet de fuego
        self.imagen_fuego = pygame.image.load('imagenes/jet25.png')
        self.rect_fuego = self.imagen_fuego.get_rect()

        # la nave empieza en el centro de abajo
        self.rect.midbottom = self.pantalla_rect.midbottom
    
    def actualizar_nave(self):
        if self.moviendose_derecha:
            self.rect.x += 1
            self.rect_fuego.x += 1
        if self.moviendose_izquierda:
            self.rect.x -= 1
            self.rect_fuego.x -= 1


    def blitme(self):
        self.pantalla.blit(self.imagen_nave, self.rect)
        self.pantalla.blit(self.imagen_fuego , self.rect)
    
