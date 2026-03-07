from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
engine = create_engine('sqlite:///terrence_m_v12.db')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    precio = Column(Float)
    cantidad = Column(Integer)

with app.app_context():
    Base.metadata.create_all(engine)

@app.route('/')
def index():
    db = SessionLocal()
    productos = db.query(Producto).all()
    total = db.query(Producto).count()
    stock = db.query(func.sum(Producto.cantidad)).scalar() or 0
    valor = db.query(func.sum(Producto.precio * Producto.cantidad)).scalar() or 0
    db.close()
    return render_template('index.html', productos=productos, total=total, stock=stock, valor=valor)

if __name__ == '__main__':
    app.run()
