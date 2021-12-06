from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect

from database import db
from forms import MenuForm
from models import Menu

app = Flask(__name__)

#configuramos la conexión a la bd
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'satv_flask_db'
FULL_URL_DB = f'postgresql://postgres:admin@localhost:5432/satv_flask_db'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Inicialización del objeto db de sqlalchemy

db.init_app(app)

#configuramos el flask-migrate

migrate = Migrate(app,db)

#Configuración de flask-wtf
app.config['SECRET_KEY'] = 'llave_secreta'

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():

    menus = Menu.query.order_by('id')
    total_menus = Menu.query.count()

    return render_template('index.html', menus=menus , total_menus = total_menus)

@app.route('/ver/<int:id>')
def ver_detalle(id):

    menu = Menu.query.get_or_404(id)
    return render_template('detalle.html', menu = menu)


@app.route('/agregar', methods= ['GET','POST'])
def agregar():

    menu = Menu()
    menuForm = MenuForm(obj=menu)

    if request.method == 'POST':
        if menuForm.validate_on_submit():
            menuForm.populate_obj(menu)
            #Insertar nuevo registro en bd con sqlalchemy
            db.session.add(menu)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html', forma = menuForm)

@app.route('/editar/<int:id>', methods = ['GET','POST'])
def editar(id):
    #Se recupera el objeto que se va a editar
    menu = Menu.query.get_or_404(id)
    menuForm = MenuForm(obj=menu)
    if request.method == 'POST':
        if menuForm.validate_on_submit():
            menuForm.populate_obj(menu)

            #Recuperar en la base de datos
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html', forma = menuForm)


@app.route('/eliminar/<int:id>')
def eliminar(id):

    menu = Menu.query.get_or_404(id)
    #Eliminamos objeto con db
    db.session.delete(menu)
    db.session.commit()
    return redirect(url_for('inicio'))




