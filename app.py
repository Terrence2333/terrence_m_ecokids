from flask import Flask, render_template_string, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Empire Hub</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; margin: 0; overflow: hidden; }
            
            /* Pantalla de Intro */
            #intro-overlay {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: #000; z-index: 9999; display: flex; align-items: center; justify-content: center;
            }
            .intro-logo {
                font-size: 4rem; font-weight: 900; color: #d4af37;
                letter-spacing: 15px; text-shadow: 0 0 30px rgba(212,175,55,0.5);
            }

            /* Contenido Principal */
            #main-content { opacity: 0; transition: opacity 2s ease; height: 100vh; display: flex; align-items: center; justify-content: center; text-align: center; }
            .gold-border { border: 1px solid #d4af37; padding: 60px; border-radius: 0; position: relative; }
        </style>
    </head>
    <body>

        <div id="intro-overlay">
            <h1 class="intro-logo animate__animated animate__zoomIn">ECO KIDS</h1>
        </div>

        <div id="main-content">
            <div class="gold-border animate__animated animate__fadeInUp">
                <p style="letter-spacing: 5px; color: #d4af37;">GLOBAL LEADERSHIP</p>
                <h1 style="font-size: 4.5rem; font-weight: 900;">TERRENCE MAYORGA</h1>
                <p class="h5 text-white-50 mb-5">INGENIERÍA SUSTENTABLE DE ÉLITE</p>
                <a href="/pay" class="btn btn-outline-warning px-5 py-3">EXPLORAR IMPERIO</a>
            </div>
        </div>

        <script>
            setTimeout(() => {
                const intro = document.getElementById('intro-overlay');
                const content = document.getElementById('main-content');
                
                intro.classList.add('animate__animated', 'animate__fadeOut');
                setTimeout(() => {
                    intro.style.display = 'none';
                    content.style.opacity = '1';
                }, 1000);
            }, 3000); // 3 segundos de intro épica
        </script>
    </body>
    </html>
    '''

@app.route('/pay')
def pay():
    return redirect('/')

if __name__ == '__main__':
    app.run()
