from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ECO KIDS | Global Elite</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
        <style>
            :root { --gold: #d4af37; --dark-bg: #050505; --accent: #28a745; }
            body { background-color: var(--dark-bg); color: #fff; font-family: 'Segoe UI', Roboto, sans-serif; overflow-x: hidden; }
            
            /* Fondo con movimiento sutil */
            .bg-gradient-custom {
                background: radial-gradient(circle at top right, #1a3a1a, transparent),
                            radial-gradient(circle at bottom left, #0a0a0a, #000);
                height: 100vh; width: 100vw; position: fixed; z-index: -1;
            }

            .hero-section { height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px; }
            
            .glass-card {
                background: rgba(255, 255, 255, 0.03);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 40px;
                padding: 60px;
                box-shadow: 0 25px 50px rgba(0,0,0,0.8);
                max-width: 900px;
                width: 100%;
            }

            .title-elite {
                font-size: 5rem;
                font-weight: 900;
                background: linear-gradient(to bottom, #fff 20%, var(--gold) 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: -2px;
            }

            .badge-director {
                display: inline-block;
                padding: 8px 20px;
                background: rgba(40, 167, 69, 0.2);
                border: 1px solid var(--accent);
                color: var(--accent);
                border-radius: 50px;
                font-size: 0.8rem;
                text-transform: uppercase;
                letter-spacing: 2px;
                margin-bottom: 20px;
            }

            .btn-gold {
                background: linear-gradient(45deg, var(--gold), #f9e29c);
                color: #000 !important;
                border: none;
                padding: 18px 45px;
                border-radius: 15px;
                font-weight: 800;
                transition: all 0.4s ease;
                text-transform: uppercase;
            }

            .btn-gold:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 30px rgba(212, 175, 55, 0.3);
            }

            footer {
                position: fixed;
                bottom: 30px;
                width: 100%;
                text-align: center;
                font-size: 0.8rem;
                color: rgba(255,255,255,0.4);
                letter-spacing: 1px;
            }
        </style>
    </head>
    <body>
        <div class="bg-gradient-custom"></div>
        
        <section class="hero-section">
            <div class="glass-card animate__animated animate__fadeInUp">
                <span class="badge-director">Executive Project</span>
                <h1 class="title-elite mb-3">ECO KIDS</h1>
                <p class="lead mb-5 text-white-50" style="font-size: 1.4rem;">
                    Redefiniendo el futuro de la educación sustentable mediante ingeniería de alta precisión y materiales reciclados.
                </p>
                
                <div class="d-flex justify-content-center gap-4">
                    <button class="btn btn-gold">Ver Catalogo Elite</button>
                    <button class="btn btn-outline-light px-5" style="border-radius: 15px;">Inversiones</button>
                </div>

                <div class="mt-5 pt-5 border-top border-white-10">
                    <p class="mb-0 text-white-50">Chief Executive Officer</p>
                    <h2 class="h4 text-white">Terrence Mayorga</h2>
                </div>
            </div>
        </section>

        <footer>
            PROPIEDAD EXCLUSIVA DE TERRENCE MAYORGA &copy; 2026 | ECO KIDS GLOBAL
        </footer>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
