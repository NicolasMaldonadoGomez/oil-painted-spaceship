import sys
import pygame

from configuracion import Configuracion
from nave import Nave

print() #espacio para ver mejor la consola

COLOR_CLARO =(220,220,220)

class Invasion:
    """Clase general donde se guarda el juego"""

    def __init__(self):
        """Inicia el objeto y crea los recursos (i.e. crea pantalla, invoca la nave"""

        self.configuracion = Configuracion()
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.configuracion.pantalla_ancho, self.configuracion.pantalla_alto))
        pygame.display.set_caption("¡¡¡INVASION!!!")
        self.nave = Nave(self)
        # Para el tema de las fps
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.SysFont("msgothic", 18)

    def corre_juego(self):
        """Empieza el bucle del juego"""
        while True:
            self.administrar_eventos()
            self.actualizar_pantalla()
    
    def administrar_eventos(self):
        for evento in pygame.event.get():                
                if evento.type == pygame.QUIT: #Espera eventos de mouse y teclado
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    self.revisar_teclas_presionadas(evento)
                elif evento.type == pygame.KEYUP:
                    self.revisar_teclas_soltadas(evento)
    
    def revisar_teclas_presionadas(self,evento):
        match evento.key: 
            case pygame.K_RIGHT:
                self.nave.moviendose_derecha = True
            case pygame.K_LEFT:
                self.nave.moviendose_izquierda = True

    def revisar_teclas_soltadas(self, evento):
        match evento.key: 
            case pygame.K_RIGHT:
                self.nave.moviendose_derecha = False
            case pygame.K_LEFT:
                self.nave.moviendose_izquierda = False
            case pygame.K_q:
                sys.exit()
            case pygame.K_ESCAPE:
                sys.exit()


    def cuenta_fps(self):
        self.fps       = str(int(self.reloj.get_fps()))
        self.texto_fps = self.fuente.render(self.fps, 1, pygame.Color(COLOR_CLARO))
        self.pantalla.blit(self.texto_fps,(0,0))
        self.reloj.tick(self.configuracion.fps)


    def actualizar_pantalla(self):
        self.nave.actualizar_nave()
        self.pantalla.fill(self.configuracion.pantalla_color)
        self.nave.dibujame()
        self.cuenta_fps()
        pygame.display.flip() #dibuja la pantalla



if __name__ == "__main__": #Solo corre si el archivo se llama directamente
    invasion = Invasion()
    invasion.corre_juego()