from flask import Flask
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

@app.route('/informacion')
def informacion():
    return "<h1>Informacion</h1>"

@app.route('/contacto')
def contacto():
    return "<h1>Contacto</h1>"

@app.route('/leguajes')
def lenguajes():
    return "<h1>Lenguajes</h1>"



if __name__ == '__main__':
    app.run(debug=True)