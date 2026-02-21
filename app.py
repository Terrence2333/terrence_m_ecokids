from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unidades')
def unidades():
    return render_template('productos.html')

@app.route('/nodos')
def nodos():
    return render_template('proyectos.html')

@app.route('/imperio')
def imperio():
    return render_template('about.html')

@app.route('/pagos')
def pagos():
    return render_template('pagos.html')

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__ == '__main__':
    app.run(debug=True)
    