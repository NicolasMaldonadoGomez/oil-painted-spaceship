import sys
import pygame

from configuracion import Configuracion
from nave import Nave
from bala import Bala
from aliens import Alien
from stars import Star


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
        #grupo para las balas
        self.balas = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.estrellas = pygame.sprite.Group()
        self._crear_flota_alienigena()
        self.crear_cielo()
        # Para el tema de las fps
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.SysFont("msgothic", 18)

    def corre_juego(self):
        """Empieza el bucle del juego"""
        while True:
            self.administrar_eventos()
            self.actualizar_pantalla()
            self.balas.update()
            self._actualiza_aliens()
    
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
            case pygame.K_LCTRL:
                self.disparar_bala()

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
    
    def disparar_bala(self):
        if len(self.balas)<self.configuracion.balas_permitidas:
            nueva_bala = Bala(self)
            self.balas.add(nueva_bala)

    def crear_cielo(self):
        for numero_fila in range(self.configuracion.estrella_filas):
            for numero_estrella in range(self.configuracion.estrella_columnas):
                estrella = Star(self, self.configuracion.espacio_entre_estrellas * numero_estrella, numero_fila * self.configuracion.espacio_entre_filas_de_estrellas)
                self.estrellas.add(estrella)

    def _crear_flota_alienigena(self):
        nuevo_alien = Alien(self)
        alien_ancho, alien_alto = nuevo_alien.rect.size
        altura_nave = self.nave.rect_nave.height
        espacio_disponible_y = (self.configuracion.pantalla_alto - 5 * alien_alto-altura_nave)
        numero_de_filas = espacio_disponible_y // ( 2 * alien_alto )
        espacio_disponible_x = self.configuracion.pantalla_ancho - 2 * alien_ancho
        columnas_de_aliens = int(espacio_disponible_x // (1.5 * alien_ancho))
        for cuenta_filas in range(numero_de_filas):
            self._crear_fila(columnas_de_aliens,cuenta_filas)


    def _crear_fila(self, columnas_de_aliens, cuenta_filas):
        for cuenta_alien in range(columnas_de_aliens):
            nuevo_alien = Alien(self)
            nuevo_alien.x = float(nuevo_alien.rect.width) * ( 1 + 1.8 * cuenta_alien )
            
            nuevo_alien.rect.x = nuevo_alien.x
            nuevo_alien.rect.y = nuevo_alien.rect.height * ( 2 + 2 * cuenta_filas)
            self.aliens.add(nuevo_alien)


    def cuenta_fps(self):
        self.fps = str(int(self.reloj.get_fps()))
        self.texto_fps = self.fuente.render(self.fps, 1, pygame.Color(COLOR_CLARO))
        self.pantalla.blit(self.texto_fps,(0,0))

        self.cantidad_balas="Balas:"+str(len(self.balas))
        self.texto_balas = self.fuente.render(self.cantidad_balas, 1, pygame.Color(COLOR_CLARO))
        self.pantalla.blit(self.texto_balas,(0,20))

        self.cantidad_aliens="Invasores:"+str(len(self.aliens))
        self.texto_aliens = self.fuente.render(self.cantidad_aliens, 1, pygame.Color(COLOR_CLARO))
        self.pantalla.blit(self.texto_aliens,(0,40))

        self.reloj.tick(self.configuracion.fps)

    def _actualiza_balas(self):
        for bala in self.balas.sprites():
            bala.dibujar_bala()
            if bala.rect.bottom<0:
                self.balas.remove(bala)
        #la siguiente linea es casi trampa, borra los sprites que se chocan
        self.colisiones = pygame.sprite.groupcollide(self.balas,self.aliens,True, True)

    def _actualiza_aliens(self):
        self.aliens.update()
        self.revisa_borde_pantalla()
            #self.Bajar_nivel_flota()
            #self.cambiar_orientacion_flota()
    
    def revisa_borde_pantalla(self):
        cambia_orientacion = False
        for alien in self.aliens.sprites():
            if alien.rect.x > (self.configuracion.pantalla_ancho-80) or  (alien.rect.x < 1):
                cambia_orientacion = True
                break
        if cambia_orientacion:
            for alien in self.aliens.sprites():
                alien.orientacion *= -1
                alien.rect.y += self.configuracion.alien_caida   


    def actualizar_pantalla(self):
        self.pantalla.fill(self.configuracion.pantalla_color)
        self.estrellas.draw(self.pantalla)
        self.nave.actualizar_nave()
        self.nave.aparecer()
        self._actualiza_balas()
        # self.actualiza_aliens()
        self.aliens.draw(self.pantalla)
        self.cuenta_fps()
        pygame.display.flip() #dibuja la pantalla



if __name__ == "__main__": #Solo corre si el archivo se llama directamente
    invasion = Invasion()
    invasion.corre_juego()