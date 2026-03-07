import os
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)

# Definimos la ruta de la base de datos de forma absoluta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, 'inventario', 'data')
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

engine = create_engine(f'sqlite:///{os.path.join(DB_DIR, "inventario.db")}')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100)); precio = Column(Float); cantidad = Column(Integer)

Base.metadata.create_all(engine)

@app.route('/')
def index():
    s = Session()
    prods = s.query(Producto).all()
    # Enviamos valores seguros para evitar errores en HTML
    total = len(prods)
    stock = sum(p.cantidad for p in prods)
    valor = sum((p.precio * p.cantidad) for p in prods)
    s.close()
    return render_template('index.html', productos=prods, total=total, stock=stock, valor=valor)

@app.route('/guardar', methods=['POST'])
def guardar():
    s = Session()
    nuevo = Producto(nombre=request.form['nombre'], cantidad=int(request.form['cantidad']), precio=float(request.form['precio']))
    s.add(nuevo); s.commit(); s.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
