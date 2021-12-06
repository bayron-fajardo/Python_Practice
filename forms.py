from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class MenuForm(FlaskForm):

    nombre = StringField('Nombre', validators=[DataRequired()])
    descipcion = TextAreaField('Descripcion')
    cantidad_unidades = IntegerField('Cantidad', validators=[DataRequired()])
    precio = IntegerField('Precio', validators=[DataRequired()])
    #Boton
    añadir = SubmitField('Añadir')
