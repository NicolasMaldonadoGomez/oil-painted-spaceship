class Configuracion:
    def __init__(self):
        self.pantalla_ancho = 1000
        self.pantalla_alto  = 1000
        self.pantalla_color = (0, 0, 0)
        self.velocidad      = 10
        self.fps             = 50
        print(vars(self))
