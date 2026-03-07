from flask import Flask, render_template, request, redirect, url_for, make_response
from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import sessionmaker, declarative_base
import pdfkit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'terrence_m_elite_v12'

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
    total_items = db.query(Producto).count()
    stock_total = db.query(func.sum(Producto.cantidad)).scalar() or 0
    valor_total = db.query(func.sum(Producto.precio * Producto.cantidad)).scalar() or 0
    db.close()
    return render_template('index.html', productos=productos, total=total_items, stock=stock_total, valor=valor_total)

@app.route('/guardar', methods=['POST'])
def guardar():
    db = SessionLocal()
    nuevo = Producto(
        nombre=request.form['nombre'],
        precio=float(request.form['precio']),
        cantidad=int(request.form['cantidad'])
    )
    db.add(nuevo)
    db.commit()
    db.close()
    return redirect(url_for('index'))

@app.route('/descargar_reporte')
def descargar_reporte():
    db = SessionLocal()
    productos = db.query(Producto).all()
    html = render_template('reporte_pdf.html', productos=productos)
    pdf = pdfkit.from_string(html, False)
    db.close()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=Reporte_Inventario.pdf'
    return response

if __name__ == '__main__':
    app.run()
