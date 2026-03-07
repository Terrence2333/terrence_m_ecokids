from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import sessionmaker, declarative_base
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'terrence_m_elite_key'

# Configuración de Base de Datos
engine = create_engine('sqlite:///terrence_m_v12.db')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    precio = Column(Float)
    cantidad = Column(Integer)
    categoria = Column(String(50))

with app.app_context():
    Base.metadata.create_all(engine)

@app.route('/')
def index():
    db = SessionLocal()
    # SUPERAMOS AL COMPAÑERO: Cálculos automáticos para el Dashboard
    total_prod = db.query(Producto).count()
    stock_total = db.query(func.sum(Producto.cantidad)).scalar() or 0
    valor_total = db.query(func.sum(Producto.precio * Producto.cantidad)).scalar() or 0
    productos = db.query(Producto).all()
    db.close()
    return render_template('index.html', total=total_prod, stock=stock_total, valor=valor_total, productos=productos)

@app.route('/guardar', methods=['POST'])
def guardar():
    db = SessionLocal()
    nuevo = Producto(
        nombre=request.form['nombre'],
        precio=float(request.form['precio']),
        cantidad=int(request.form['cantidad']),
        categoria=request.form.get('categoria', 'General')
    )
    db.add(nuevo)
    db.commit()
    db.close()
    return redirect(url_for('index'))

# SUPERAMOS AL COMPAÑERO: Exportación masiva en un solo click
@app.route('/exportar/<formato>')
def exportar(formato):
    db = SessionLocal()
    prods = db.query(Producto).all()
    data = [{"nombre": p.nombre, "precio": p.precio, "cantidad": p.cantidad} for p in prods]
    db.close()
    
    if formato == 'json':
        return jsonify(data)
    return "Formato CSV/TXT en desarrollo para Tarea 12"

if __name__ == '__main__':
    app.run(debug=True)
