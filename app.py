import csv, json, os
from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
# Configuración persistente
engine = create_engine('sqlite:///inventario/data/inventario.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    precio = Column(Float)

Base.metadata.create_all(engine)

@app.route('/')
def index():
    session = Session()
    productos = session.query(Producto).all()
    session.close()
    return render_template('index.html', productos=productos)

@app.route('/guardar', methods=['POST'])
def guardar():
    n, p = request.form['nombre'], float(request.form['precio'])
    # SQL
    s = Session()
    s.add(Producto(nombre=n, precio=p)); s.commit(); s.close()
    # TXT
    with open('inventario/data/datos.txt', 'a') as f: f.write(f"{n},{p}\n")
    # CSV
    with open('inventario/data/datos.csv', 'a', newline='') as f:
        csv.writer(f).writerow([n, p])
    # JSON
    d = {"nombre": n, "precio": p}
    lista = []
    if os.path.exists('inventario/data/datos.json'):
        with open('inventario/data/datos.json', 'r') as f:
            try: lista = json.load(f)
            except: lista = []
    lista.append(d)
    with open('inventario/data/datos.json', 'w') as f: json.dump(lista, f)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
