import sys
import pygame

from configuracion import Configuracion
from nave import Nave

print() #espacio para ver mejor la consola

class Invasion:
    """Clase general donde se guarda el juego"""

    def __init__(self):
        """Inicia el objeto y crea los recursos (i.e. crea pantalla, invoca la nave"""

        self.configuracion = Configuracion()
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.configuracion.pantalla_ancho, self.configuracion.pantalla_alto))
        pygame.display.set_caption("¡¡¡INVASION!!!")
        self.nave = Nave(self)

    def corre_juego(self):
        """Empieza el bucle del juego"""
        while True:
            self.administrar_eventos()
            self.actualizar_pantalla()
    
    def administrar_eventos(self):
        for event in pygame.event.get():                
                if event.type == pygame.QUIT: #Espera eventos de mouse y teclado
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    match event.key: 
                        case pygame.K_RIGHT:
                            self.nave.moviendose_derecha = True
                        case pygame.K_LEFT:
                            self.nave.moviendose_izquierda = True
                elif event.type == pygame.KEYUP:
                    match event.key: 
                        case pygame.K_RIGHT:
                            self.nave.moviendose_derecha = False
                        case pygame.K_LEFT:
                            self.nave.moviendose_izquierda = False

    def actualizar_pantalla(self):
        self.nave.actualizar_nave()
        self.pantalla.fill(self.configuracion.pantalla_color)
        self.nave.blitme()
        pygame.display.flip() #dibuja la pantalla



if __name__ == "__main__": #Solo corre si el archivo se llama directamente
    invasion = Invasion()
    invasion.corre_juego()