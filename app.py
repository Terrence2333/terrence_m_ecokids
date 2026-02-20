import os
from flask import Flask, render_template_string, request, session, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'ECO_KIDS_ELITE_2026'

# Conexión Profesional a PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Executive</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
            .gold-card { border: 1px solid #d4af37; padding: 60px; border-radius: 40px; background: rgba(10,10,10,0.9); box-shadow: 0 0 80px rgba(212, 175, 55, 0.1); text-align: center; }
            .name-brand { font-size: 4rem; font-weight: 900; color: #d4af37; letter-spacing: -2px; }
            .btn-elite { background: #d4af37; color: #000; font-weight: 800; border: none; padding: 15px 40px; border-radius: 10px; text-decoration: none; display: inline-block; transition: 0.3s; }
            .btn-elite:hover { background: #fff; transform: translateY(-3px); }
        </style>
    </head>
    <body>
        <div class="gold-card">
            <p style="color: #666; letter-spacing: 5px;">EXCLUSIVE PLATFORM</p>
            <h1 class="name-brand mb-4">ECO KIDS</h1>
            <h2 class="h5 mb-5 text-white-50">BY TERRENCE MAYORGA</h2>
            <a href="/login" class="btn-elite">SISTEMA ADMINISTRATIVO</a>
        </div>
    </body>
    </html>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aquí puedes definir tu acceso único
        if request.form['user'] == 'terrence' and request.form['pass'] == 'elite2026':
            session['admin'] = True
            return "BIENVENIDO, DIRECTOR MAYORGA. ACCESO TOTAL CONCEDIDO."
        return "ACCESO DENEGADO. CREDENCIALES INVÁLIDAS."
    
    return '''
    <body style="background:#000; color:#d4af37; display:flex; align-items:center; justify-content:center; height:100vh; font-family:sans-serif;">
        <form method="POST" style="border:1px solid #333; padding:40px; border-radius:20px; text-align:center;">
            <h3>SISTEMA DE SEGURIDAD</h3>
            <input type="text" name="user" placeholder="Usuario" style="display:block; margin:20px auto; padding:10px; background:#111; border:1px solid #d4af37; color:#fff;">
            <input type="password" name="pass" placeholder="Password" style="display:block; margin:20px auto; padding:10px; background:#111; border:1px solid #d4af37; color:#fff;">
            <button type="submit" style="background:#d4af37; color:#000; border:none; padding:10px 30px; cursor:pointer; font-weight:bold;">INGRESAR</button>
        </form>
    </body>
    '''

if __name__ == '__main__':
    app.run()
