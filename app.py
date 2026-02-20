from flask import Flask, render_template_string, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Cosmos</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; margin: 0; overflow: hidden; }
            
            /* Contenedor de Partículas */
            #particles-js {
                position: fixed; width: 100%; height: 100%; top: 0; left: 0;
                background-color: #000; background-image: url(''); background-repeat: no-repeat;
                background-size: cover; background-position: 50% 50%; z-index: -1;
            }

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
            #main-content {
                opacity: 0; transition: opacity 2s ease; height: 100vh;
                display: flex; align-items: center; justify-content: center; text-align: center;
                position: relative; z-index: 1; /* Para que el contenido esté sobre las partículas */
            }
            .gold-border { border: 1px solid #d4af37; padding: 60px; border-radius: 0; position: relative; }
        </style>
    </head>
    <body>

        <div id="particles-js"></div>

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

        <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
        <script>
            // Configuración de partículas doradas y sutiles
            particlesJS('particles-js', {
                "particles": {
                    "number": { "value": 80, "density": { "enable": true, "value_area": 800 } },
                    "color": { "value": "#d4af37" },
                    "shape": { "type": "circle" },
                    "opacity": { "value": 0.5, "random": false, "anim": { "enable": false } },
                    "size": { "value": 3, "random": true, "anim": { "enable": false } },
                    "line_linked": {
                        "enable": true, "distance": 150, "color": "#666", "opacity": 0.4, "width": 1
                    },
                    "move": {
                        "enable": true, "speed": 2, "direction": "none", "random": false,
                        "straight": false, "out_mode": "out", "bounce": false,
                        "attract": { "enable": false, "rotateX": 600, "rotateY": 1200 }
                    }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": {
                        "onhover": { "enable": true, "mode": "grab" },
                        "onclick": { "enable": true, "mode": "push" },
                        "resize": true
                    },
                    "modes": {
                        "grab": { "distance": 140, "line_linked": { "opacity": 1 } },
                        "bubble": { "distance": 400, "size": 40, "duration": 2, "opacity": 8, "speed": 3 },
                        "repulse": { "distance": 200, "duration": 0.4 },
                        "push": { "particles_nb": 4 },
                        "remove": { "particles_nb": 2 }
                    }
                },
                "retina_detect": true
            });

            // Lógica de Intro Cinematic
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
