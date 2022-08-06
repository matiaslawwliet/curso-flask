from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')  #Home
def index():
    return render_template('index.html', titulo="Inicio")

@app.route('/sobrenosotros')  #Sobre Nosotros
def sobrenosotros():
    return render_template('sobre-nosotros.html', titulo="Sobre Nosotros")

@app.route('/contacto')  #Contacto
def contacto():
    return render_template('contacto.html', titulo="Contacto")

app.run(debug=True)
