import sys

import pygame
from configuracion import Configuracion as Confi
from nave import Nave

print() #espacio para ver mejor la consola

class Invasion:
    """Clase general donde se guarda el juego"""

    def __init__(self):
        """Inicia el objeto y crea los recursos"""

        self.confi = Confi()
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.confi.pantalla_ancho, self.confi.pantalla_alto))
        pygame.display.set_caption("¡¡¡INVASION!!!")
        self.nave = Nave(self)

    def corre_juego(self):
        """Empieza el bucle del juego"""
        while True:
            for event in pygame.event.get():                
                if event.type == pygame.QUIT: #Espera eventos de mouse y teclado
                    sys.exit()
            self.pantalla.fill(self.confi.pantalla_color)
            self.nave.blitme()

            pygame.display.flip() #dibuja la pantalla


if __name__ == "__main__": #Solo corre si el archivo se llama directamente
    invasion = Invasion()
    invasion.corre_juego()