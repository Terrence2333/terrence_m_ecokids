#!/bin/bash
# SCRIPT DE CONTROL TOTAL - TERRENCE.M OS -> GITHUB -> RENDER

beep_siren() {
    echo -e "\a"
    sleep 0.1
    echo -e "\a"
}

echo -e "\033[31m[!] INICIANDO DESPLIEGUE GLOBAL TERRENCE.M OS...\033[0m"
beep_siren

# 1. Preparar directorios y Backups
mkdir -p templates static backups logs
if [ -f "templates/index.html" ]; then
    cp templates/index.html backups/index_backup_$(date +"%Y%m%d_%H%M%S").html
    echo -e "\033[32m[OK]\033[0m Backup local creado."
fi

# 2. Inyectar el código con Radar y Botón de Pánico (ESC)
cat << 'INDEX' > templates/index.html
{% extends "base.html" %}
{% block content %}
<canvas id="noise-canvas" style="position: fixed; inset: 0; z-index: 20000; pointer-events: none; opacity: 0; transition: opacity 0.1s;"></canvas>
<div id="boot-screen" style="position: fixed; inset: 0; background: #000; z-index: 10000; display: flex; flex-direction: column; justify-content: center; align-items: center; font-family: 'Orbitron', sans-serif; color: #d4af37;">
    <div id="loader-ring" style="width: 140px; height: 140px; border: 5px solid #ff4500; border-radius: 50%; animation: spin 0.5s linear infinite;"></div>
    <p style="letter-spacing: 10px; margin-top: 20px;">SYNCING_RENDER_OS...</p>
</div>
<div id="main-interface" style="padding: 50px; opacity: 0; visibility: hidden; transition: opacity 1s;">
    <h1 style="color: #d4af37; font-family: 'Orbitron'; font-weight: 900;">TERRENCE M - SECURE LINK</h1>
    <div style="background: rgba(255,69,0,0.1); border: 1px solid #ff4500; padding: 20px; color: #fff;">
        SISTEMA ACTUALIZADO: RADAR + PÁNICO (ESC) ACTIVOS
    </div>
</div>
<script>
    window.addEventListener('keydown', (e) => { if (e.key === "Escape") location.reload(); });
    window.addEventListener('DOMContentLoaded', () => {
        setTimeout(() => {
            document.getElementById('boot-screen').style.display = 'none';
            document.getElementById('main-interface').style.visibility = 'visible';
            document.getElementById('main-interface').style.opacity = '1';
        }, 1000);
    });
</script>
{% endblock %}
INDEX

# 3. Sincronización Automática con GitHub
echo -e "\033[34m[GIT]\033[0m Subiendo cambios a GitHub para Render..."
git add .
git commit -m "Auto-Deploy: Terrence.M OS v.$(date +'%Y.%m.%d.%H%M')"
git push origin main

echo -e "\033[33m-----------------------------------------------\033[0m"
echo -e "\033[32mDESPLIEGUE FINALIZADO. REVISE SU URL EN RENDER.\033[0m"
echo -e "\033[33m-----------------------------------------------\033[0m"
beep_siren
