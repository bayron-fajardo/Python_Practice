from flask import Flask, request, render_template, url_for, jsonify, session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

#Añadir clave secreta:
app.secret_key = 'Mi_llave_secreta'



@app.route('/')
def inicio():
    if 'username' in session:
        return f'El usuario {session["username"]}, ya ha hecho login'
    return 'no ha hecho login '

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #Se omitió la validación de usuario y contraseña
        usuario = request.form['username'] #mismo valor que en el formulario html
        #Agregar usuario a la sesión
        session['username'] = usuario
        #Opcion simplificada:
        #session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

#Eliminar sesion.
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es : {edad}'

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)

#Redireccionar a otra página e incluir valores <>

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Juan' ))

@app.route('/salir')
def salir():
    return abort(404)
#Personalizar paginas de error


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404 #Codigo de estado 404


#REST Representational state transfer
@app.route('/api/mostrar/<nombre>', methods = ['POST', 'GET'])
def mostrar_json(nombre):
    valores ={ 'nombre' : nombre, 'metodo_http' : request.method}
    return jsonify(valores)


