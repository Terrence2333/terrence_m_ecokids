from flask import Flask, render_template_string, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Payment Hub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://www.paypal.com/sdk/js?client-id=sb&currency=USD"></script>
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
            .hub-card { background: #0a0a0a; border: 2px solid #d4af37; padding: 40px; border-radius: 40px; text-align: center; box-shadow: 0 0 60px rgba(212,175,55,0.15); max-width: 600px; width: 100%; }
            .price-tag { font-size: 3.5rem; font-weight: 900; color: #d4af37; margin: 10px 0; }
            .payment-method { background: #111; border: 1px solid #333; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
            .btc-btn { background: #f7931a; color: #fff; font-weight: bold; border: none; padding: 12px; border-radius: 8px; width: 100%; text-transform: uppercase; }
        </style>
    </head>
    <body>
        <div class="hub-card">
            <p style="letter-spacing:5px; color:#666; font-size: 0.8rem;">TERRENCE MAYORGA GLOBAL SYSTEMS</p>
            <h1 class="h2 mb-0">CENTRO DE PAGOS ELITE</h1>
            <div class="price-tag">$150.00</div>
            
            <div class="payment-method">
                <div id="paypal-button-container"></div>
            </div>

            <div class="payment-method">
                <button class="btc-btn" onclick="window.location.href='/success'">
                    Pagar con Bitcoin (Simulación)
                </button>
            </div>
        </div>

        <script>
            paypal.Buttons({
                createOrder: function(data, actions) {
                    return actions.order.create({ purchase_units: [{ amount: { value: '150.00' } }] });
                },
                onApprove: function(data, actions) {
                    return actions.order.capture().then(function(details) {
                        window.location.href = "/success";
                    });
                }
            }).render('#paypal-button-container');
        </script>
    </body>
    </html>
    '''

@app.route('/success')
def success():
    return '''
    <body style="background:#000; color:#fff; font-family:sans-serif; display:flex; align-items:center; justify-content:center; height:100vh; text-align:center;">
        <div style="border:1px solid #d4af37; padding:50px; border-radius:30px; max-width:500px;">
            <h1 style="color:#d4af37;">¡PAGO CONFIRMADO!</h1>
            <p style="font-size:1.2rem; margin:20px 0;">Gracias por tu adquisición en ECO KIDS.</p>
            <div style="background:#111; padding:20px; border-radius:10px; margin-bottom:30px;">
                <p style="color:#888; margin:0;">PRÓXIMO PASO:</p>
                <p>Un asesor de logística de Terrence Mayorga se contactará contigo en menos de 24 horas para coordinar la entrega de tu Kit Pro.</p>
            </div>
            <a href="/" style="color:#d4af37; text-decoration:none; font-weight:bold;">VOLVER AL INICIO</a>
        </div>
    </body>
    '''

if __name__ == '__main__':
    app.run()
