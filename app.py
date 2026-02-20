import os
from flask import Flask, render_template_string, request, session, redirect

app = Flask(__name__)
app.secret_key = 'ECO_KIDS_ELITE_2026'

# Base de Datos de Visitas Simbolica (Nivel Dios)
stats = {"visitas": 1250, "paises": 12, "proyectos": 45}

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Elite Intelligence</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; min-height: 100vh; }
            .hero { height: 70vh; display: flex; align-items: center; justify-content: center; text-align: center; background: radial-gradient(circle, #111, #000); }
            .gold-text { color: #d4af37; font-weight: 900; letter-spacing: -2px; font-size: 5rem; }
            .stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 40px; max-width: 1000px; margin: -100px auto 0; }
            .stat-card { background: rgba(255,255,255,0.05); backdrop-filter: blur(15px); border: 1px solid rgba(212,175,55,0.2); padding: 30px; border-radius: 25px; text-align: center; }
            .stat-number { font-size: 2.5rem; color: #d4af37; font-weight: bold; }
            .stat-label { color: #666; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 2px; }
            .nav-elite { padding: 20px; border-bottom: 1px solid #222; display: flex; justify-content: space-between; align-items: center; }
        </style>
    </head>
    <body>
        <nav class="nav-elite">
            <span style="color:#d4af37; font-weight:bold; letter-spacing:3px;">ECO KIDS</span>
            <span style="color:#444; font-size:0.8rem;">DIRECTOR: TERRENCE MAYORGA</span>
        </nav>
        
        <section class="hero">
            <div class="animate__animated animate__fadeIn">
                <p class="text-white-50">SISTEMA GLOBAL DE MONITOREO</p>
                <h1 class="gold-text">DATA CENTER</h1>
            </div>
        </section>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">''' + str(stats['visitas']) + '''</div>
                <div class="stat-label">Impacto Global</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">''' + str(stats['paises']) + '''</div>
                <div class="stat-label">Naciones Activas</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">''' + str(stats['proyectos']) + '''</div>
                <div class="stat-label">Ingeniería Eco</div>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
