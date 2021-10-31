class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0  for i in range(numero) ]

    def ingresar_dato(self):
        self.datos  = [int(input('Ingresar datos:  ' + str(i+1) + ' = ')) for i in range(self.n)]


class Operaciones_Basicas(Calculadora):
    def __init__(self):
        super().__init__(self, 2)

    def suma(self):
        a,b, = self.datos
        suma = a + b
        print(f'El resultado de la suma es: {suma}')


    def resta(self):
        a,b, = self.datos
        resta = a - b
        print(f'EL resultado de la resta : {resta}')

class Operaciones_intermedias(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def multiplicar(self):
        a,b, = self.datos
        multi = a * b
        print(f' El resultado de la multiplicación es: {multi}')

    def dividir(self):
        try:
            a,b, = self.datos
            dividir = a / b
            print(f'El resultado de la división es de : {dividir}')

        except:
            print('No se puede dividir entre 0')

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a , = self.datos
        print(f' El resultado es : {math.sqrt(a)}')

prueba1 = Operaciones_intermedias()
print(prueba1.ingresar_dato())
print(prueba1.dividir())