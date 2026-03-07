from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import os

app = Flask(__name__)
# Configuración base de datos
engine = create_engine('sqlite:///inventario/data/inventario.db')
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
    # Definimos explícitamente las variables para que el HTML no falle
    total = len(prods)
    stock = sum(p.cantidad for p in prods)
    valor = sum(p.precio * p.cantidad for p in prods)
    s.close()
    return render_template('index.html', productos=prods, total=total, stock=stock, valor=valor)

@app.route('/guardar', methods=['POST'])
def guardar():
    s = Session()
    nuevo = Producto(nombre=request.form['nombre'], cantidad=int(request.form['cantidad']), precio=float(request.form['precio']))
    s.add(nuevo); s.commit(); s.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
