from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
app.config['SECRET_KEY'] = 'terrence_m_secret'

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

with app.app_context():
    Base.metadata.create_all(engine)

@app.route('/')
def index():
    # Esto cargará su index.html real de la carpeta templates
    return render_template('index.html')

@app.route('/productos')
def ver_productos():
    # Esto activará su archivo productos.html que ya existe
    return render_template('productos.html')

@app.route('/datos')
def ver_datos():
    # Esto activará su archivo datos.html
    return render_template('datos.html')

@app.route('/proyectos')
def ver_proyectos():
    return render_template('proyectos.html')

if __name__ == '__main__':
    app.run()
