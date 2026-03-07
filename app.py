from flask import Flask, render_template, request, redirect, url_for, make_response
from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import sessionmaker, declarative_base
import pdfkit

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

@app.route('/guardar', methods=['POST'])
def guardar():
    db = SessionLocal()
    nuevo = Producto(nombre=request.form['nombre'], precio=float(request.form['precio']), cantidad=int(request.form['cantidad']))
    db.add(nuevo); db.commit(); db.close()
    return redirect(url_for('index'))

@app.route('/descargar_reporte')
def descargar_reporte():
    db = SessionLocal(); productos = db.query(Producto).all(); db.close()
    html = render_template('reporte_pdf.html', productos=productos)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=Reporte_Elite.pdf'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
