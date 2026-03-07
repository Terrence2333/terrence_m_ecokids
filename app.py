from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/terrence.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    visa = db.Column(db.String(100))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context(): db.create_all()

@app.route('/')
def index():
    return render_template('index.html', regs=Registro.query.order_by(Registro.id.desc()).all())

@app.route('/agregar', methods=['POST'])
def agregar():
    db.session.add(Registro(nombre=request.form['nombre'], visa=request.form['visa']))
    db.session.commit()
    return redirect('/')

if __name__ == '__main__': app.run()
