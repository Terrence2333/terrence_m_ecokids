import os
from flask import Flask, render_template_string, request, session, redirect, jsonify

app = Flask(__name__)
app.secret_key = 'ECO_KIDS_ELITE_2026'

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head><link rel="icon" href="https://cdn-icons-png.flaticon.com/512/1598/1598196.png" type="image/x-icon">
        <meta charset="UTF-8">
        <title>ECO KIDS | Global Elite AI</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #000; color: #fff; font-family: 'Inter', sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
            .gold-card { border: 1px solid #d4af37; padding: 60px; border-radius: 40px; background: rgba(10,10,10,0.9); box-shadow: 0 0 80px rgba(212,175,55,0.1); text-align: center; position: relative; }
            .name-brand { font-size: 4rem; font-weight: 900; color: #d4af37; letter-spacing: -2px; }
            
            /* Chatbot Elegante */
            #chat-bot { position: fixed; bottom: 30px; right: 30px; width: 350px; background: #111; border: 1px solid #d4af37; border-radius: 20px; display: none; flex-direction: column; box-shadow: 0 10px 30px rgba(0,0,0,0.5); z-index: 1000; }
            #chat-header { background: #d4af37; color: #000; padding: 15px; border-radius: 18px 18px 0 0; font-weight: bold; }
            #chat-box { height: 300px; overflow-y: auto; padding: 15px; font-size: 0.9rem; }
            #chat-input { background: #222; border: none; padding: 15px; color: #fff; border-top: 1px solid #333; width: 100%; border-radius: 0 0 20px 20px; }
            .chat-btn { position: fixed; bottom: 30px; right: 30px; background: #d4af37; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; border: none; font-size: 24px; box-shadow: 0 5px 15px rgba(212,175,55,0.4); }
        </style>
    </head>
    <body>
        <div class="gold-card">
            <p style="color: #666; letter-spacing: 5px;">AI-POWERED PLATFORM</p>
            <h1 class="name-brand mb-4">ECO KIDS</h1>
            <h2 class="h5 mb-5 text-white-50">BY TERRENCE MAYORGA</h2>
            <button class="btn btn-outline-warning px-5" style="border-radius: 50px;">PROYECTOS ELITE</button>
        </div>

        <button class="chat-btn" onclick="toggleChat()">🤖</button>

        <div id="chat-bot">
            <div id="chat-header">Asistente Virtual ECO KIDS</div>
            <div id="chat-box" id="messages"></div>
            <input type="text" id="chat-input" placeholder="Pregunta sobre ECO KIDS..." onkeypress="handleChat(event)">
        </div>

        <script>
            function toggleChat() { 
                const chat = document.getElementById('chat-bot');
                chat.style.display = chat.style.display === 'flex' ? 'none' : 'flex';
            }
            function handleChat(e) {
                if(e.key === 'Enter') {
                    const box = document.getElementById('chat-box');
                    const input = document.getElementById('chat-input');
                    box.innerHTML += `<p><b>Tú:</b> ${input.value}</p>`;
                    setTimeout(() => {
                        box.innerHTML += `<p style="color:#d4af37"><b>IA:</b> Hola, soy el asistente de Terrence Mayorga. Estamos transformando el reciclaje en educación de élite.</p>`;
                        box.scrollTop = box.scrollHeight;
                    }, 1000);
                    input.value = '';
                }
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
