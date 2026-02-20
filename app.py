from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Hub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; }
            .hub-card { background: #0a0a0a; border: 1px solid #d4af37; padding: 50px; border-radius: 40px; text-align: center; box-shadow: 0 0 50px rgba(212,175,55,0.1); }
            .btn-gold { background: #d4af37; color: #000; font-weight: bold; padding: 15px 40px; border-radius: 10px; text-decoration: none; display: inline-block; }
        </style>
    </head>
    <body>
        <div class="hub-card">
            <h1 style="color:#d4af37; font-weight:900;">ECO KIDS</h1>
            <p class="mb-5 text-white-50">SISTEMA LIDERADO POR TERRENCE MAYORGA</p>
            <a href="/pay" class="btn-gold">ADQUIRIR KIT PRO</a>
        </div>
    </body>
    </html>
    '''

@app.route('/pay')
def pay():
    return '''
    <body style="background:#000; color:#fff; display:flex; align-items:center; justify-content:center; height:100vh; font-family:sans-serif;">
        <div style="text-align:center; border:1px solid #333; padding:40px; border-radius:20px;">
            <h2 style="color:#d4af37;">MÓDULO DE PAGO</h2>
            <p>Simulación de Transacción Segura</p>
            <button onclick="window.location.href='/success'" style="background:#d4af37; padding:10px 20px; border:none; cursor:pointer; font-weight:bold;">CONFIRMAR PAGO $150</button>
        </div>
    </body>
    '''

@app.route('/success')
def success():
    return '''
    <body style="background:#000; color:#fff; font-family:sans-serif; padding:50px;">
        <div style="max-width:600px; margin:0 auto; border:1px solid #d4af37; padding:40px; border-radius:20px; text-align:center;">
            <h1 style="color:#d4af37;">¡PAGO EXITOSO!</h1>
            <p>Gracias por confiar en la ingeniería de Terrence Mayorga.</p>
            <hr style="border-color:#222; margin:30px 0;">
            <h3>¿NECESITAS AYUDA CON TU PEDIDO?</h3>
            <p class="text-white-50">Genera un ticket de soporte inmediato:</p>
            <form action="/ticket" method="POST">
                <input type="text" name="asunto" placeholder="Asunto (Ej: Envío, Factura)" required style="width:100%; padding:10px; margin-bottom:10px; background:#111; border:1px solid #333; color:#fff;">
                <textarea name="mensaje" placeholder="Describe tu duda aquí..." required style="width:100%; padding:10px; height:100px; background:#111; border:1px solid #333; color:#fff;"></textarea>
                <button type="submit" style="background:#fff; color:#000; border:none; padding:10px 30px; font-weight:bold; margin-top:10px; cursor:pointer;">ENVIAR TICKET</button>
            </form>
        </div>
    </body>
    '''

@app.route('/ticket', methods=['POST'])
def ticket():
    # En una app real, esto se guarda en la DB de Render
    return '''
    <body style="background:#000; color:#d4af37; display:flex; align-items:center; justify-content:center; height:100vh; font-family:sans-serif; text-align:center;">
        <div>
            <h1>TICKET GENERADO #EK-2026</h1>
            <p style="color:#fff;">Director Terrence Mayorga ha recibido tu mensaje. Responderemos a la brevedad.</p>
            <a href="/" style="color:#d4af37; text-decoration:none;">Volver al Panel Principal</a>
        </div>
    </body>
    '''

if __name__ == '__main__':
    app.run()
