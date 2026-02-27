from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "terrence_m.db"

# --- POO: CLASES ---
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id, self._nombre, self._cantidad, self._precio = id, nombre, cantidad, precio
    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def get_cantidad(self): return self._cantidad
    def get_precio(self): return self._precio

class Cliente:
    def __init__(self, id, nombre, rango):
        self._id, self._nombre, self._rango = id, nombre, rango
    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def get_rango(self): return self._rango

# --- GESTIÓN DE BASE DE DATOS ---
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS productos (id TEXT PRIMARY KEY, nombre TEXT, cantidad INTEGER, precio REAL)")
        conn.execute("CREATE TABLE IF NOT EXISTS clientes (id TEXT PRIMARY KEY, nombre TEXT, rango TEXT)")

@app.route('/')
def index(): return render_template('index.html')

@app.route('/unidades')
def unidades():
    with sqlite3.connect(DB_NAME) as conn:
        prods = [Producto(f[0], f[1], f[2], f[3]) for f in conn.execute("SELECT * FROM productos")]
    return render_template('productos.html', productos=prods)

@app.route('/imperio')
def imperio(): return render_template('about.html')

@app.route('/nodos')
def nodos(): return render_template('proyectos.html')

@app.route('/pagos')
def pagos(): return render_template('pagos.html')

@app.route('/exito')
def exito(): return render_template('exito.html')

@app.route('/add_item', methods=['POST'])
def add_item():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT OR REPLACE INTO productos VALUES (?,?,?,?)", 
                     (request.form['id'], request.form['nombre'], int(request.form['cantidad']), float(request.form['precio'])))
    return redirect(url_for('unidades'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
