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
    nombre = Column(String(100)); precio = Column(Float); cantidad = Column(Integer)

Base.metadata.create_all(engine)

@app.route('/')
def index():
    s = Session(); prods = s.query(Producto).all(); s.close()
    return render_template('index.html', productos=prods)

@app.route('/productos')
def productos():
    s = Session(); prods = s.query(Producto).all(); s.close()
    return render_template('productos.html', productos=prods)

@app.route('/datos')
def datos():
    return render_template('datos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
