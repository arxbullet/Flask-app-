from flask import Flask, url_for, redirect, render_template
from datetime import datetime
#inicio 
#1. instalar flask  : pip install Flask
#2. crear archivo main en carpeta en donde instalamos Flask
#3. iniciar app con python main.py
#instanciar app y frmawork para usarlo
app = Flask(__name__)

@app.context_processor
def date_now():
    return{
        'now':datetime.utcnow()
    }

#crear ruta app

@app.route('/')
def index(): # el nombre de la ruta es el nombre de la funcion
    return render_template('index.html')

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
    if redireccion is not None:
        return redirect(url_for('lenguajes'))
   # return "<h1>Contacto</h1>"
    return render_template('contacto.html')

@app.route('/lenguajes')
def lenguajes():
    return render_template('lenguajes.html', 
                            dato1='dato1',
                            dato2='dato2')
    
    #return "<h1>Lenguajes</h1>"

if __name__ == '__main__':
    app.run(debug=True)