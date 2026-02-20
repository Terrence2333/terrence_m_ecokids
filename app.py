from flask import Flask, render_template
import os

app = Flask(__name__)

# Ruta principal que acepta GET y las verificaciones HEAD de Render
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pagos')
def pagos():
    return render_template('pagos.html')

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__ == '__main__':
    # Forzamos el puerto 10000 para evitar que Render detenga el servicio
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)