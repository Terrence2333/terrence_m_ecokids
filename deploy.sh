#!/bin/bash
# SCRIPT DE CONTROL TOTAL: TERRENCE.M OS -> GITHUB -> RENDER

# Configuración del Director
SERVICE_NAME="terrence.m"
RENDER_URL="https://$SERVICE_NAME.onrender.com"

beep_siren() {
    echo -e "\a"
    sleep 0.1
    echo -e "\a"
}

echo -e "\033[31m[!] INICIANDO DESPLIEGUE GLOBAL EN RENDER...\033[0m"
beep_siren

# 1. Preparar directorios y Backups
mkdir -p templates static backups logs
if [ -f "templates/index.html" ]; then
    cp templates/index.html backups/index_backup_$(date +"%Y%m%d_%H%M%S").html
    echo -e "\033[32m[OK]\033[0m Backup local de seguridad creado."
fi

# 2. Inyectar el código con Radar, Pánico (ESC) y Sismógrafo
cat << 'INDEX' > templates/index.html
{% extends "base.html" %}
{% block content %}
<canvas id="noise-canvas" style="position: fixed; inset: 0; z-index: 20000; pointer-events: none; opacity: 0; transition: opacity 0.1s;"></canvas>
<div id="boot-screen" style="position: fixed; inset: 0; background: #000; z-index: 10000; display: flex; flex-direction: column; justify-content: center; align-items: center; font-family: 'Orbitron', sans-serif; color: #d4af37;">
    <div id="loader-ring" style="width: 120px; height: 120px; border: 2px solid #ff4500; border-radius: 50%; animation: spin 0.5s linear infinite;"></div>
    <p style="letter-spacing: 10px; margin-top: 20px; font-size: 0.7rem;">ESTABLECIENDO ENLACE CON RENDER...</p>
</div>
<div id="main-interface" style="padding: 50px; opacity: 0; visibility: hidden; transition: opacity 1s;">
    <h1 style="color: #d4af37; font-family: 'Orbitron'; font-weight: 900;">TERRENCE M - LIVE SYSTEM</h1>
    <div style="background: rgba(255,69,0,0.1); border: 1px solid #ff4500; padding: 25px; color: #fff; font-family: monospace;">
        <p>[ SISTEMA OPERATIVO EN LÍNEA ]</p>
        <p>> PROTOCOLO DE PÁNICO: [ESC] ACTIVO</p>
        <p>> RADAR SÍSMICO: CALIBRADO</p>
    </div>
</div>
<script>
    window.addEventListener('keydown', (e) => { 
        if (e.key === "Escape") {
            document.getElementById('noise-canvas').style.opacity = "1";
            setTimeout(() => { location.reload(); }, 500);
        }
    });
    window.addEventListener('DOMContentLoaded', () => {
        setTimeout(() => {
            document.getElementById('boot-screen').style.display = 'none';
            document.getElementById('main-interface').style.visibility = 'visible';
            document.getElementById('main-interface').style.opacity = '1';
        }, 1500);
    });
</script>
{% endblock %}
INDEX

# 3. Sincronización Automática con GitHub
echo -e "\033[34m[GIT]\033[0m Sincronizando repositorio..."
git add .
git commit -m "Render-Deploy: Terrence.M OS $(date +'%H:%M:%S')"
git push origin main

# 4. Finalización y enlace
echo -e "\033[33m-----------------------------------------------\033[0m"
echo -e "\033[32mDESPLIEGUE ENVIADO EXITOSAMENTE A RENDER.\033[0m"
echo -e "\033[36mURL DE ACCESO:\033[0m \033[4m$RENDER_URL\033[0m"
echo -e "\033[33m-----------------------------------------------\033[0m"
beep_siren
