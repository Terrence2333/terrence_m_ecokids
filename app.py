import os
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'ECO_KIDS_ELITE_2026_SECURE_TOKEN')

# Bloque de Seguridad: Forzar redirección a HTTPS (SSL)
@app.before_request
def force_https():
    if not request.is_secure and os.environ.get('FLASK_ENV') != 'development':
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Secure Platform</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
            .secure-badge { color: #d4af37; font-size: 0.7rem; letter-spacing: 5px; margin-bottom: 20px; }
            .hub-card { border: 1px solid #d4af37; padding: 60px; border-radius: 50px; background: rgba(10,10,10,0.95); text-align: center; box-shadow: 0 0 100px rgba(212,175,55,0.2); }
            .status-online { display: inline-block; width: 10px; height: 10px; background: #00ff00; border-radius: 50%; margin-right: 10px; box-shadow: 0 0 10px #00ff00; }
        </style>
    </head>
    <body>
        <div class="hub-card">
            <div class="secure-badge">SSL ENCRYPTED SYSTEM</div>
            <h1 style="font-weight:900; color:#d4af37; font-size: 3.5rem;">ECO KIDS</h1>
            <p style="color:#666; letter-spacing: 3px;">DIRECTOR GENERAL: TERRENCE MAYORGA</p>
            <div class="mt-5">
                <span class="status-online"></span>
                <span style="font-size: 0.8rem; color: #aaa; text-transform: uppercase;">Servidores Activos y Protegidos</span>
            </div>
            <hr style="border-color: #222; margin: 40px 0;">
            <a href="/pay" class="btn btn-outline-warning px-5 py-3" style="border-radius:10px; font-weight:bold;">INGRESAR AL HUB DE PAGOS</a>
        </div>
    </body>
    </html>
    '''

@app.route('/pay')
def pay():
    return redirect('/')

if __name__ == '__main__':
    app.run()
