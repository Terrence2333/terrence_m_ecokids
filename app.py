import os
from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Conexión a la base de datos de Render (Nivel Dios)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Perfil del Director Único
class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), default='Terrence Mayorga')

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
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; overflow: hidden; }
            .elite-container { height: 100vh; display: flex; align-items: center; justify-content: center; background: radial-gradient(circle at center, #111 0%, #000 100%); }
            .gold-border { border: 2px solid #d4af37; padding: 50px; border-radius: 0 50px 0 50px; background: rgba(20,20,20,0.8); box-shadow: 0 0 50px rgba(212, 175, 55, 0.2); }
            .name-title { font-size: 4.5rem; font-weight: 900; letter-spacing: -3px; color: #d4af37; }
            .btn-pro { background: #d4af37; color: #000; font-weight: bold; padding: 15px 40px; border: none; text-transform: uppercase; }
        </style>
    </head>
    <body>
        <div class="elite-container">
            <div class="gold-border text-center">
                <p class="text-uppercase mb-0" style="letter-spacing: 5px; color: #666;">CEO & Founder</p>
                <h1 class="name-title mb-4">TERRENCE MAYORGA</h1>
                <div class="mb-5" style="height: 2px; background: #d4af37; width: 100px; margin: 0 auto;"></div>
                <h2 class="h4 mb-5 text-white-50">ECO KIDS GLOBAL ENTERPRISE</h2>
                <button class="btn-pro">Acceder al Sistema</button>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
