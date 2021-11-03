class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

class Bicicleta(Coche):
    def __init__(self,velocidad,tipo):
        super().__init__(velocidad)
        self.tipo = tipo


