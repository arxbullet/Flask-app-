from flask import Flask, flash ,url_for, redirect, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL 
#inicio 
#1. instalar flask  : pip install Flask
#2. crear archivo main en carpeta en donde instalamos Flask
#3. iniciar app con python main.py
#instanciar app y frmawork para usarlo
app = Flask(__name__)
#Para usar my sql primero debo instalar pip install flask-mysqldb

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)

app.secret_key = 'clave secreta de flask'

@app.context_processor
def date_now():
    return{
        'now':datetime.utcnow()
    }

#crear ruta app

@app.route('/')
def index(): # el nombre de la ruta es el nombre de la funcion
    edad = 18

    return render_template('index.html', 
                            edad=edad)

#parametro opcional
@app.route('/informacion')
#parametro obligatorio
@app.route('/informacion/<string:nombre>')
def informacion(nombre = 'default'):
    #return f"<h1>Hola, {nombre}:Informacion</h1>"
    return render_template('informacion.html', nombre = nombre)

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):
    personas = ['juan', 'pedro', 'diego']
    if redireccion is not None:
        return redirect(url_for('lenguajes'))
   # return "<h1>Contacto</h1>"
    return render_template('contacto.html', 
                            personas = personas)

@app.route('/lenguajes')
def lenguajes():
    return render_template('lenguajes.html', 
                            dato1='dato1',
                            dato2='dato2')
    
    #return "<h1>Lenguajes</h1>"

@app.route('/crear-coche', methods=['GET','POST'])
def crear_coche():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        precio= request.form['precio']
        ciudad = request.form['ciudad']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO auto VALUES(NULL, %s, %s, %s, %s)",(marca, modelo, precio, ciudad))
        cursor.connection.commit()
        flash('has creado el coche correctamente')
        return redirect(url_for('index'))
    return render_template('crear_coche.html')

if __name__ == '__main__':
    app.run(debug=True)