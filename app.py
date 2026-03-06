from flask import Flask, render_template, request, redirect, url_for, flash
from inventario.bd import init_db, SessionLocal
from inventario.productos import Producto
from form import ProductoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'terrence_m_secret'

with app.app_context():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/lista")
def lista():
    db = SessionLocal()
    productos = db.query(Producto).all()
    db.close()
    return str([p.nombre for p in productos])

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    form = ProductoForm()
    if form.validate_on_submit():
        db = SessionLocal()
        nuevo_producto = Producto(
            nombre=form.nombre.data,
            precio=form.precio.data,
            cantidad=form.cantidad.data,
            email_proveedor=form.email_proveedor.data
        )
        db.add(nuevo_producto)
        db.commit()
        db.close()
        return redirect(url_for('productos'))
    return render_template('producto_form.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
