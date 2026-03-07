import csv, json, os
from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
engine = create_engine('sqlite:///inventario/data/inventario.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    precio = Column(Float)
    cantidad = Column(Integer)

Base.metadata.create_all(engine)

@app.route('/')
def index():
    s = Session()
    prods = s.query(Producto).all()
    # Estadísticas para el Dashboard
    total = len(prods)
    stock = sum(p.cantidad for p in prods)
    valor = sum(p.precio * p.cantidad for p in prods)
    s.close()
    return render_template('index.html', productos=prods, total=total, stock=stock, valor=valor)

@app.route('/guardar', methods=['POST'])
def guardar():
    n, c, p = request.form['nombre'], int(request.form['cantidad']), float(request.form['precio'])
    # SQL
    s = Session()
    s.add(Producto(nombre=n, cantidad=c, precio=p))
    s.commit(); s.close()
    # Archivos (Persistencia punto 2.2)
    with open('inventario/data/datos.txt', 'a') as f: f.write(f"{n},{c},{p}\n")
    with open('inventario/data/datos.csv', 'a', newline='') as f: csv.writer(f).writerow([n, c, p])
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
