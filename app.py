from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
app.config['SECRET_KEY'] = 'terrence_m_secret'

# Base de datos
engine = create_engine('sqlite:///terrence_m.db')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)
    cantidad = Column(Integer)
    email_proveedor = Column(String)

# Forzar creación de tablas al arrancar
with app.app_context():
    Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lista')
def lista():
    db = SessionLocal()
    productos = db.query(Producto).all()
    db.close()
    return "Productos en sistema: " + str([p.nombre for p in productos])

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
        return "Producto agregado correctamente"
    return render_template('producto_form.html')

if __name__ == '__main__':
    app.run()
