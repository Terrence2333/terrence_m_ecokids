import os
import stripe
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)
app.secret_key = 'ECO_KIDS_ELITE_2026'

# Configura tus llaves de Stripe aquí
stripe.api_key = "sk_test_51T2ydpEAXn9FETRf..."

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Checkout Elite</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; }
            .payment-card { background: #0a0a0a; border: 1px solid #d4af37; padding: 50px; border-radius: 30px; text-align: center; box-shadow: 0 0 50px rgba(212,175,55,0.2); }
            .price { font-size: 3rem; color: #d4af37; font-weight: 900; margin: 20px 0; }
            .btn-pay { background: #d4af37; color: #000; font-weight: bold; width: 100%; padding: 15px; border-radius: 10px; border: none; text-transform: uppercase; }
        </style>
    </head>
    <body>
        <div class="payment-card">
            <p style="letter-spacing:3px; color:#666;">ORDEN DE COMPRA EXCLUSIVA</p>
            <h1 class="h3">PROYECTO ECO-INGENIERÍA</h1>
            <div class="price">$150.00 USD</div>
            <p class="text-white-50 mb-5">Adquiere el kit completo supervisado por Terrence Mayorga.</p>
            
            <form action="/create-checkout-session" method="POST">
                <button type="submit" class="btn-pay">Pagar de Forma Segura</button>
            </form>
            
            <div class="mt-4 small text-secondary">Procesado por Stripe &reg;</div>
        </div>
    </body>
    </html>
    '''

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': 'Kit Eco Kids Pro'},
                    'unit_amount': 15000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://terrence-m-ecokids.onrender.com/success',
            cancel_url='https://terrence-m-ecokids.onrender.com/cancel',
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
