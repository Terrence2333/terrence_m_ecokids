from flask import Flask, render_template_string

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
            .payment-method { background: #111; border: 1px solid #333; padding: 20px; border-radius: 15px; margin-bottom: 20px; transition: 0.3s; }
            .payment-method:hover { border-color: #d4af37; transform: translateY(-5px); }
            .btc-btn { background: #f7931a; color: #fff; font-weight: bold; border: none; padding: 12px; border-radius: 8px; width: 100%; text-transform: uppercase; }
        </style>
    </head>
    <body>
        <div class="hub-card">
            <p style="letter-spacing:5px; color:#666; font-size: 0.8rem;">TERRENCE MAYORGA GLOBAL SYSTEMS</p>
            <h1 class="h2 mb-0">CENTRO DE PAGOS ELITE</h1>
            <div class="price-tag">$150.00</div>
            
            <div class="payment-method">
                <p class="small text-white-50">Opción A: Pago Global & Ecuador</p>
                <div id="paypal-button-container"></div>
            </div>

            <div class="payment-method">
                <p class="small text-white-50">Opción B: Activos Digitales</p>
                <button class="btc-btn" onclick="alert('DIRECCIÓN BTC DE TERRENCE: bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0w7h')">
                    Pagar con Bitcoin (BTC)
                </button>
            </div>

            <div class="payment-method">
                <p class="small text-white-50">Opción C: Stripe (Crédito/Débito)</p>
                <button class="btn btn-outline-light w-100 py-2" style="border-radius:8px;">Continuar con Tarjeta</button>
            </div>

            <p class="mt-4" style="color:#d4af37; font-size: 0.7rem; letter-spacing: 2px;">PROTEGIDO POR CIFRADO NIVEL DIOS</p>
        </div>

        <script>
            paypal.Buttons({
                createOrder: function(data, actions) {
                    return actions.order.create({
                        purchase_units: [{ amount: { value: '150.00' } }]
                    });
                },
                onApprove: function(data, actions) {
                    return actions.order.capture().then(function(details) {
                        alert('¡TRANSACCIÓN EXITOSA! Bienvenido a ECO KIDS, ' + details.payer.name.given_name);
                    });
                }
            }).render('#paypal-button-container');
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
