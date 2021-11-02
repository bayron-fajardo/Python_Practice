class MiClase:

    variable_clase = 'Valor variable clase'


    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)


    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)



miobjeto1 = MiClase('Variable_instancia')
miobjeto1.metodo_clase()
 



