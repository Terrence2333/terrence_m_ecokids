import os
from flask import Flask, render_template_string, request, flash

app = Flask(__name__)
app.secret_key = 'ECO_KIDS_ELITE_2026'

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Elite Network</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; }
            .vip-section { height: 100vh; display: flex; align-items: center; justify-content: center; background: radial-gradient(circle at center, #111 0%, #000 100%); }
            .gold-form { background: rgba(255,255,255,0.02); border: 1px solid #d4af37; padding: 60px; border-radius: 40px; box-shadow: 0 0 100px rgba(212,175,55,0.1); max-width: 600px; width: 100%; text-align: center; }
            .input-elite { background: transparent; border: none; border-bottom: 2px solid #333; color: #fff; padding: 15px; width: 100%; margin-bottom: 30px; text-align: center; transition: 0.4s; }
            .input-elite:focus { outline: none; border-bottom-color: #d4af37; }
            .btn-vip { background: #d4af37; color: #000; font-weight: 900; border: none; padding: 15px 50px; border-radius: 5px; text-transform: uppercase; letter-spacing: 2px; }
            .director-tag { color: #d4af37; font-size: 0.8rem; letter-spacing: 4px; margin-bottom: 10px; display: block; }
        </style>
    </head>
    <body>
        <div class="vip-section">
            <div class="gold-form">
                <span class="director-tag">TERRENCE MAYORGA PRESENTS</span>
                <h1 class="mb-4" style="font-weight:900;">VIP ACCESS</h1>
                <p class="text-white-50 mb-5">Únete a la red exclusiva de ingeniería sustentable ECO KIDS.</p>
                <form action="/subscribe" method="POST">
                    <input type="email" name="email" class="input-elite" placeholder="Tu Correo Electrónico Corporativo" required>
                    <button type="submit" class="btn-vip">Solicitar Membresía</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    # Aquí los correos se guardarían en tu base de datos profesional
    return f'''
    <body style="background:#000; color:#d4af37; display:flex; align-items:center; justify-content:center; height:100vh; font-family:sans-serif; text-align:center;">
        <div>
            <h1>REGISTRO EXITOSO</h1>
            <p style="color:#fff;">El correo {email} ha sido añadido a la lista privada de Terrence Mayorga.</p>
            <a href="/" style="color:#d4af37; text-decoration:none; border:1px solid #d4af37; padding:10px 20px;">VOLVER</a>
        </div>
    </body>
    '''

if __name__ == '__main__':
    app.run()
