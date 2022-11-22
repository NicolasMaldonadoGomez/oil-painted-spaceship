import pygame

class Nave:
    """Con esta clase manejamos la nave"""
    def __init__(self, invasion_juego,):
        """inicializa la nave y establece la posicion inicial"""
        self.pantalla = invasion_juego.pantalla
        self.pantalla_rect = invasion_juego.pantalla.get_rect()

        # cargamos la imagen
        self.imagen = pygame.image.load(imagenes/nave25.png)
        self.rect = self.imagen.get_rect()

        # la nave empieza en el centro de abajo
        self.rect.midbottom = self.screen_rect.midbottom

        def blitme(self):
            self.pantalla.blit(self.imagen, self.rect)
    
