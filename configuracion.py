class Configuracion:
    def __init__(self):
        self.pantalla_ancho = 1000
        self.pantalla_alto  = 1000
        self.pantalla_color = (50, 50, 50)

configura = {
    'pantalla_ancho' : 1000,
    'pantalla_alto' : 1000,
    'pantalla_color' : (50, 50, 50)
}

for k,v in configura.items():
    print(f"El valor de {k} es {v}")

print('Fin de la confiuración\n')