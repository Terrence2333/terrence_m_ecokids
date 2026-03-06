cat <<EOF > app.py
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'terrence_m_secret'

# Base de datos local para render
db_path = 'terrence_m.db'
engine = create_engine(f'sqlite:///{db_path}')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)
    cantidad = Column(Integer)
    email_proveedor = Column(String)

Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lista')
def lista():
    db = SessionLocal()
    productos = db.query(Producto).all()
    lista_productos = [f"{p.nombre} - ${p.precio}" for p in productos]
    db.close()
    return str(lista_productos)

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        db = SessionLocal()
        nuevo = Producto(
            nombre=request.form['nombre'],
            precio=float(request.form['precio']),
            cantidad=int(request.form['cantidad']),
            email_proveedor=request.form['email_proveedor']
        )
        db.add(nuevo)
        db.commit()
        db.close()
        return redirect(url_for('productos'))
    return render_template('producto_form.html')

if __name__ == '__main__':
    app.run(debug=True)
EOF