from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Empire</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
            .aura { position: absolute; width: 100%; height: 100%; background: radial-gradient(circle, rgba(212,175,55,0.05) 0%, transparent 70%); z-index: -1; }
            .brand-box { border-left: 5px solid #d4af37; padding-left: 30px; }
            .glitch { font-size: 5rem; font-weight: 900; color: #d4af37; text-transform: uppercase; letter-spacing: 10px; }
        </style>
    </head>
    <body>
        <div class="aura"></div>
        <div class="brand-box">
            <p style="letter-spacing: 8px; color: #444;">ESTABLISHED 2026</p>
            <h1 class="glitch">ECO KIDS</h1>
            <p class="h4 text-white-50">BY TERRENCE MAYORGA</p>
            <div class="mt-5">
                <a href="/pay" class="btn btn-warning btn-lg px-5" style="border-radius: 0; font-weight: bold;">ACCESO ELITE</a>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/director')
def director():
    return '''
    <body style="background:#050505; color:#0f0; font-family:'Courier New', monospace; padding:50px;">
        <h1 style="border-bottom: 1px solid #0f0; padding-bottom:10px;">> TERRENCE_M_OS_v1.0</h1>
        <div style="margin-top:30px;">
            <p>[+] SISTEMA: ONLINE</p>
            <p>[+] BASE DE DATOS: CONECTADA (ECUADOR-HUB)</p>
            <p>[+] TRÁFICO: 1.2k VISITAS ACTIVAS</p>
            <p>[+] INGRESOS: $150.00 USD (PENDIENTE DE COBRO)</p>
            <p style="color:#d4af37;">[!] ALERTA: NUEVA SOLICITUD DE MEMBRESÍA VIP</p>
        </div>
        <div style="margin-top:50px;">
            <input type="text" placeholder="Escribir comando..." style="background:transparent; border:none; color:#0f0; width:100%; outline:none;">
        </div>
    </body>
    '''

@app.route('/pay')
def pay():
    return redirect('/')

if __name__ == '__main__':
    app.run()
