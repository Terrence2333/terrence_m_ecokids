from flask import Flask, render_template_string, request, redirect
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_SET_URL'] = 'sqlite:///ecokids_elite.db'
db = SQLAlchemy(app)

# Modelo de Base de Datos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Elite System</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #050505; color: white; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
            .main-frame { background: rgba(255,255,255,0.02); backdrop-filter: blur(30px); border: 1px solid rgba(212, 175, 55, 0.2); border-radius: 40px; padding: 60px; text-align: center; box-shadow: 0 0 80px rgba(0,0,0,1); position: relative; }
            .gold-brand { font-size: 4rem; font-weight: 900; background: linear-gradient(45deg, #fff, #d4af37); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .btn-elite { background: #d4af37; color: black; font-weight: bold; border-radius: 12px; padding: 15px 40px; border: none; transition: 0.3s; margin-top: 20px; }
            .btn-elite:hover { background: #fff; transform: scale(1.05); }
            .ceo-tag { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: #d4af37; color: black; padding: 5px 20px; border-radius: 50px; font-size: 0.7rem; font-weight: bold; letter-spacing: 2px; }
        </style>
    </head>
    <body>
        <div class="main-frame">
            <div class="ceo-tag">OFFICIAL PLATFORM</div>
            <h1 class="gold-brand">ECO KIDS</h1>
            <p class="text-white-50 lead mb-5">Sistema Central de Gestión de Juguetes Sustentables</p>
            <div class="d-grid gap-3">
                <button class="btn-elite">ACCESO DIRECTOR GENERAL</button>
                <small class="text-secondary mt-4">Desarrollado y Supervisado por: <br><strong>Terrence Mayorga</strong></small>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
