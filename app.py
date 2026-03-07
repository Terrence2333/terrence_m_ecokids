import os
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
# Rutas relativas para que funcione en cualquier entorno
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
    s = Session(); prods = s.query(Producto).all()
    t = len(prods); st = sum(p.cantidad for p in prods); v = sum(p.precio * p.cantidad for p in prods)
    s.close()
    return render_template('index.html', productos=prods, total=t, stock=st, valor=v)

@app.route('/guardar', methods=['POST'])
def guardar():
    s = Session()
    s.add(Producto(nombre=request.form['nombre'], cantidad=int(request.form['cantidad']), precio=float(request.form['precio'])))
    s.commit(); s.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
