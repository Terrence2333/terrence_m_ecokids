#!/bin/bash
# SCRIPT DE DESPLIEGUE TERRENCE.M OS - PANIC EDITION

beep_siren() {
    echo -e "\a"
    sleep 0.1
    echo -e "\a"
}

echo -e "\033[31m[!] INSTALANDO PROTOCOLO DE PÁNICO 'ESC'...\033[0m"
beep_siren

mkdir -p templates static backups logs
touch logs/intruders.log logs/system_load.log

# Backup
if [ -f "templates/index.html" ]; then
    cp templates/index.html backups/index_backup_$(date +"%Y%m%d_%H%M%S").html
fi

# Inyectar Interfaz con Listener de Teclado
cat << 'INDEX' > templates/index.html
{% extends "base.html" %}
{% block content %}
<canvas id="noise-canvas" style="position: fixed; inset: 0; z-index: 20000; pointer-events: none; opacity: 0; transition: opacity 0.1s;"></canvas>

<div id="boot-screen" style="position: fixed; inset: 0; background: #000; z-index: 10000; display: flex; flex-direction: column; justify-content: center; align-items: center; font-family: 'Orbitron', sans-serif; color: #d4af37;">
    <div id="loader-ring" style="width: 140px; height: 140px; border: 1px solid #111; border-top: 5px solid #ff4500; border-radius: 50%; animation: spin 0.4s linear infinite;"></div>
    <p style="font-size: 0.55rem; letter-spacing: 15px; margin-top: 25px; color: #d4af37;">PANIC_BUTTON_READY [ESC] : <span id="percent">0</span>%</p>
</div>

<div id="main-interface" style="display: flex; justify-content: space-between; padding: 40px 5%; height: 85vh; position: relative; z-index: 1; opacity: 0; visibility: hidden; transition: opacity 1s, filter 0.2s;">
    <div style="width: 320px;">
        <div id="core-circle" style="position: relative; width: 260px; height: 260px; border: 4px solid #d4af37; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.95);">
            <h1 style="font-size: 2.3rem; font-weight: 900; color: #d4af37;">TERRENCE M</h1>
        </div>
        <div style="margin-top: 40px; background: rgba(0,0,0,0.9); border-left: 10px solid #ff4500; padding: 25px;">
            <p style="color:#ff4500; font-weight: 900; font-size: 0.7rem;">[ SECURITY_LEVEL: MAX ]</p>
            <div style="font-family: 'Orbitron'; color: #0f0; font-size: 0.8rem;">TECLA ESC: ACTIVA</div>
        </div>
    </div>

    <div id="chat-container" style="position:fixed; bottom:80px; right:30px; width:430px; background:rgba(0,0,0,0.95); border:2px solid #ff4500; z-index:1000; visibility: hidden;">
        <div id="chat-box" style="height:250px; overflow-y:auto; padding:20px; font-size:0.7rem; color:#fff; font-family: monospace;"></div>
        <div style="display:flex; border-top:1px solid #ff4500;">
            <input type="text" id="user-input" placeholder="ORDEN..." style="flex:1; background:#000; border:none; color:#fff; padding:15px; outline:none;">
            <button onclick="sendMessage()" style="background:#ff4500; border:none; padding:0 25px; cursor:pointer;">EXE</button>
        </div>
    </div>
</div>

<script>
    const noise = document.getElementById('noise-canvas');
    const nCtx = noise.getContext('2d');
    noise.width = window.innerWidth; noise.height = window.innerHeight;

    function triggerPanic() {
        noise.style.opacity = "0.9";
        document.getElementById('main-interface').style.filter = "contrast(3) invert(1) blur(10px)";
        const imgData = nCtx.createImageData(noise.width, noise.height);
        for (let i = 0; i < imgData.data.length; i += 4) {
            const v = Math.random() * 255;
            imgData.data[i] = v; imgData.data[i+1] = 0; imgData.data[i+2] = 0; imgData.data[i+3] = 255;
        }
        nCtx.putImageData(imgData, 0, 0);
        setTimeout(() => { location.reload(); }, 2000);
    }

    // LISTENER DE BOTÓN DE PÁNICO (ESC)
    window.addEventListener('keydown', (e) => {
        if (e.key === "Escape") {
            console.log("PANIC TRIGGERED");
            triggerPanic();
        }
    });

    function sendMessage() {
        const v = document.getElementById('user-input').value.toLowerCase();
        if(v.includes("admin") || v.includes("hack")) triggerPanic();
        document.getElementById('chat-box').innerHTML += `<p style="color:#ff4500">> ${v}</p>`;
        document.getElementById('user-input').value = "";
    }

    window.addEventListener('DOMContentLoaded', () => {
        setTimeout(() => {
            document.getElementById('boot-screen').style.display = 'none';
            document.getElementById('main-interface').style.visibility = 'visible';
            document.getElementById('main-interface').style.opacity = '1';
            document.getElementById('chat-container').style.visibility = 'visible';
        }, 1000);
    });
</script>
{% endblock %}
INDEX

chmod 644 templates/index.html
chmod +x deploy.sh
echo -e "\033[33m-----------------------------------------------\033[0m"
echo -e "\033[31mPANIC BUTTON (ESC) ACTIVADO - SISTEMA LISTO\033[0m"
echo -e "\033[33m-----------------------------------------------\033[0m"
beep_siren
