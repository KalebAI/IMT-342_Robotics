#!/usr/bin/env bash
set -e

# 1) Descargar e instalar Miniconda en modo batch
cd /tmp
curl -LO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p "$HOME/miniconda3"   # -b = silencioso
# Inicializar conda en bash
source "$HOME/miniconda3/bin/activate"
conda init bash

# 2) Crear/actualizar entorno
cd - >/dev/null
conda env update -n robotics -f environment.yml || conda env create -f environment.yml
echo "✅ Miniconda + entorno 'robotics' listo. Abre una nueva terminal o ejecuta:  conda activate robotics"
