from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Professional</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #0a0a0a; color: white; font-family: sans-serif; }
            .hero { height: 100vh; display: flex; align-items: center; justify-content: center; background: linear-gradient(45deg, #000 30%, #1a1a1a 100%); }
            .glass-card { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.1); border-radius: 30px; padding: 50px; text-align: center; }
            .gold-text { color: #d4af37; text-transform: uppercase; letter-spacing: 5px; }
            .btn-premium { background: #28a745; border: none; padding: 15px 40px; border-radius: 50px; color: white; font-weight: bold; transition: 0.4s; }
            .btn-premium:hover { background: #1e7e34; transform: scale(1.05); }
        </style>
    </head>
    <body>
        <div class="hero">
            <div class="glass-card">
                <h1 class="display-1 gold-text">ECO KIDS</h1>
                <p class="lead mb-5">Ingeniería en Juguetes Educativos Sustentables</p>
                <button class="btn-premium">EXPLORAR PROYECTOS</button>
                <div class="mt-5 pt-5 border-top border-secondary">
                    <p class="small text-secondary">Director del Proyecto</p>
                    <h3 class="h5">Terrence Mayorga</h3>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
