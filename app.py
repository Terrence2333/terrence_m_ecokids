from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return render_template('index.html')

@app.route('/pagos')
def pagos():
    return render_template('pagos.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__ == '__main__':
    # Render usa la variable PORT, si no existe usa el 10000 por defecto
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
