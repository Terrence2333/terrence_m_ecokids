from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index(): return render_template('index.html')

@app.route('/about')
def about(): return render_template('about.html')

@app.route('/servicios')
def servicios(): return render_template('servicios.html')

@app.route('/proyectos')
def proyectos(): return render_template('proyectos.html')

@app.route('/pagos')
def pagos(): return render_template('pagos.html')

@app.route('/exito')
def exito(): return render_template('exito.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
    