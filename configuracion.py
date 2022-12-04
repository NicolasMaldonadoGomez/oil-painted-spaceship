class Configuracion:
    def __init__(self):
        self.pantalla_ancho     = 1250
        self.pantalla_alto      = 1000
        self.pantalla_color     = (0, 0, 0)
        self.velocidad          = 10
        self.fps                = 50
        self.tamaño_propulsores = (20,150)
        self.tamaño_aliens      = (90,25)
        self.bala_velocidad     = 16.0
        self.bala_ancho         = 3
        self.bala_alto          = 10
        self.bala_color         = (220, 150, 150)
        self.balas_permitidas   = 3
        self.estrella_filas     = 15
        self.estrella_columnas  = 15
        self.estrella_tamaño    = 25

        '''configuracion calculadas'''

        self.espacio_entre_estrellas = self.pantalla_ancho // self.estrella_columnas
        self.espacio_entre_filas_de_estrellas = self.pantalla_alto// self.estrella_filas
        # print() #espacio para ver mejor la consola
        # print(vars(self))
        # print() #espacio para ver mejor la consola

