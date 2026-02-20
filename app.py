import os
from flask import Flask, render_template_string, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'ECO_KIDS_ELITE_2026'
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegurar que la carpeta de fotos exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configuración de Base de Datos
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
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
            .gold-card { border: 1px solid #d4af37; padding: 60px; border-radius: 40px; background: rgba(10,10,10,0.9); box-shadow: 0 0 80px rgba(212,175,55,0.1); text-align: center; }
            .name-brand { font-size: 4rem; font-weight: 900; color: #d4af37; letter-spacing: -2px; }
            .btn-elite { background: #d4af37; color: #000; font-weight: 800; border: none; padding: 15px 40px; border-radius: 10px; text-decoration: none; display: inline-block; transition: 0.3s; }
        </style>
    </head>
    <body>
        <div class="gold-card">
            <p style="color: #666; letter-spacing: 5px;">EXCLUSIVE PLATFORM</p>
            <h1 class="name-brand mb-4">ECO KIDS</h1>
            <h2 class="h5 mb-5 text-white-50">BY TERRENCE MAYORGA</h2>
            <a href="/admin" class="btn-elite">PANEL DE CONTROL</a>
        </div>
    </body>
    </html>
    '''

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form.get('user') == 'terrence' and request.form.get('pass') == 'elite2026':
            session['admin'] = True
    
    if not session.get('admin'):
        return '''
        <body style="background:#000; color:#d4af37; display:flex; align-items:center; justify-content:center; height:100vh; font-family:sans-serif;">
            <form method="POST" style="border:1px solid #333; padding:40px; border-radius:20px; text-align:center;">
                <h3>ACCESO RESTRINGIDO - MAYORGA</h3>
                <input type="text" name="user" placeholder="Usuario" style="display:block; margin:20px auto; padding:10px; background:#111; border:1px solid #d4af37; color:#fff;">
                <input type="password" name="pass" placeholder="Password" style="display:block; margin:20px auto; padding:10px; background:#111; border:1px solid #d4af37; color:#fff;">
                <button type="submit" style="background:#d4af37; color:#000; border:none; padding:10px 30px; cursor:pointer; font-weight:bold;">DESBLOQUEAR</button>
            </form>
        </body>
        '''
    
    return '''
    <body style="background:#050505; color:#fff; padding:50px; font-family:sans-serif;">
        <h1 style="color:#d4af37;">Panel de Gestión - Terrence Mayorga</h1>
        <hr style="border-color:#333;">
        <h3>Subir Nuevo Proyecto de Juguete</h3>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" style="margin-bottom:20px;">
            <button type="submit" style="background:#28a745; color:#fff; border:none; padding:10px 20px;">SUBIR A LA NUBE</button>
        </form>
        <br><a href="/logout" style="color:red;">Cerrar Sesión Segura</a>
    </body>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if not session.get('admin'): return redirect('/')
    if 'file' not in request.files: return 'No hay archivo'
    file = request.files['file']
    if file.filename == '': return 'Sin nombre'
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'ARCHIVO SUBIDO CON ÉXITO AL SISTEMA ECO KIDS.'

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/')

if __name__ == '__main__':
    app.run()
