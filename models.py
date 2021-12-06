from app import db


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))
    descipcion = db.Column(db.String(500))
    cantidad_unidades = db.Column(db.Integer)
    precio = db.Column(db.Integer)

    def __str__(self):
        return {
            f'Id: {self.id},'
            f'Nombre: {self.nombre},'
            f'Descripción: {self.descipcion},'
            f'Cantidad de unidades: {self.cantidad_unidades},'
            f'Precio : ${self.precio}'
        }

