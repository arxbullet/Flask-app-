from django.shortcuts import redirect
from flask import Flask, url_for
#inicio 
#1. instalar flask  : pip install Flask
#2. crear archivo main en carpeta en donde instalamos Flask
#3. iniciar app con python main.py
#instanciar app y frmawork para usarlo
app = Flask(__name__)

#crear ruta app

@app.route('/')
def index(): # el nombre de la ruta es el nombre de la funcion
    return"aprendiendo flask"

#parametro opcional
@app.route('/informacion')
#parametro obligatorio
@app.route('/informacion/<string:nombre>')
def informacion(nombre = 'default'):
    return f"<h1>Hola, {nombre}:Informacion</h1>"


@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):

    if redireccion is not None:
        return redirect(url_for('lenguajes'))

    return "<h1>Contacto</h1>"

@app.route('/lenguajes')
def lenguajes():
    return "<h1>Lenguajes</h1>"

if __name__ == '__main__':
    app.run(debug=True)