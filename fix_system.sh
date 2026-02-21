#!/bin/bash
# SCRIPT DE REPARACIÓN DE EMERGENCIA - TERRENCE.M OS

echo -e "\033[31m[!] INICIANDO REPARACIÓN DE NÚCLEO Y LIMPIEZA DE CACHÉ...\033[0m"

# 1. Limpiar archivos temporales y asegurar permisos
rm -rf __pycache__
chmod -R 755 static/ templates/
echo -e "\033[32m[OK]\033[0m Permisos restaurados."

# 2. Forzar actualización de punteros de Git
git rm -r --cached . > /dev/null 2>&1
git add .
echo -e "\033[32m[OK]\033[0m Índice de archivos regenerado."

# 3. Commit de Recuperación
git commit -m "System Fix: Hard Reset & Cache Clear $(date +'%T')"

# 4. Empujar con fuerza al servidor
echo -e "\033[34m[GIT]\033[0m Forzando despliegue en Render..."
git push origin main --force

echo -e "\033[33m-----------------------------------------------\033[0m"
echo -e "\033[32mSISTEMA REPARADO. ESPERE 60 SEGUNDOS Y RECARGUE.\033[0m"
echo -e "\033[33m-----------------------------------------------\033[0m"
