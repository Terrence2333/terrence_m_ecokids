import os
from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
# Usamos una ruta absoluta para que Render no pierda los datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'inventario', 'data', 'inventario.db')
engine = create_engine(f'sqlite:///{DB_PATH}')
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
    productos = s.query(Producto).all()
    total = len(productos)
    stock = sum(p.cantidad for p in productos)
    valor = sum(p.precio * p.cantidad for p in productos)
    s.close()
    return render_template('index.html', productos=productos, total=total, stock=stock, valor=valor)

@app.route('/guardar', methods=['POST'])
def guardar():
    s = Session()
    nuevo = Producto(nombre=request.form['nombre'], cantidad=int(request.form['cantidad']), precio=float(request.form['precio']))
    s.add(nuevo); s.commit(); s.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
