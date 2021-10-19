# encoding: utf-8
#      ____                            _             __     ___     _
#    / ___|___  _ __ ___  _ __  _   _| |_ ___ _ __  \ \   / (_)___(_) ___  _ __
#   | |   / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|  \ \ / /| / __| |/ _ \| '_ \
#   | |__| (_) | | | | | | |_) | |_| | ||  __/ |      \ V / | \__ \ | (_) | | | |
#    \____\___/|_| |_| |_| .__/ \__,_|\__\___|_|       \_/  |_|___/_|\___/|_| |_|
#                        |_|
#       _    ____  ____            _  _____ _
#      / \  |  _ \|  _ \  __   __ / ||___  | |_
#     / _ \ | |_) | |_) | \ \ / / | |   / /| __|
#    / ___ \|  __/|  __/   \ V /  | |_ / / | |_
#   /_/   \_\_|   |_|       \_/   |_(_)_/   \__|
#
#
# Computer Vision APP
# Creado por @flowese versión: 1.7 para terminal.
# Reconocimiento de objetos en tiempo real para fuentes de video.
# Fichero actual: style.py
# En este fichero se almacenan las funciones, elementos y variables de estilo.

# LIBRERÍAS
import pyfiglet
import time
import sys
import time
import os
from datetime import datetime

# FUNCION LIMPIAR PANTALLA TERMINAL


def limpiarterminal():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")


# CONVERSIÓN DE TEXTOS A ASCI-ART PARA TITULOS
def convertoasci(texto_asci):
    texto_asci = pyfiglet.figlet_format(texto_asci)
    return texto_asci

# BARRA DE CARGA


def mostrar_cargando():
    animacion_barras = ["                             ■□□□□□□□□□", "                             ■■□□□□□□□□", "                             ■■■□□□□□□□", "                             ■■■■□□□□□□", "                             ■■■■■□□□□□", "                             ■■■■■■□□□□",
                        "                             ■■■■■■■□□□", "                             ■■■■■■■□□□", "                             ■■■■■■■□□□", "                             ■■■■■■■■□□", "                             ■■■■■■■■■□", "                             ■■■■■■■■■■"]
    # - Animar la barra
    for i in range(len(animacion_barras)):
        time.sleep(0.6)
        sys.stdout.write("\r" + animacion_barras[i % len(animacion_barras)])
        sys.stdout.flush()
    return animacion_barras


# TEXTOS

# Textos del terminal
def imprtextos(introducido):
    if introducido == 'inicio':
        print('Computer Vision APP (2021) - Creado por @flowese miembro de #HubSpain.com\n')
        print('· Este modelo está entrenado y funciona sin internet.\n')
        print('· El modelo "Rapido" puede ejecutarse en Raspberry pi de forma óptima. \n')
        print('· Es compatible con CPU y GPU (con drivers NVIDIA CUDA). \n')
    elif introducido == 'modelo':
        url_drivers = ("(más info en: https://developer.nvidia.com/cuda-zone)")
        print('~ Los modelos de inteligencia artificial se utilizan para el reconocimiento de obejtos. \n')
        print('~ Para utilizar estos modelos con GPU requieren tener instalados los drivers de NVIDIA CUDA. ' '\n' ' ', (url_drivers), '\n')
        print('~ El modelo "Rapido" está optimizado para funcionar con Raspberry pi aunque es menos preciso.\n')
        print('~ Usar el modelo "Preciso" es el más recomendable pero requiere mas procesamiento. \n')
    elif introducido == 'consola':
        tiempo = datetime.now()
        # - Formato d/mm/YY H:M:S
        dt_string = tiempo.strftime("%d/%m/%Y %H:%M:%S")
        print('CVAPP LIVE FEED.', '-', dt_string, '\n')
        print('Configuración actual: \n')
    elif introducido == 'final':
        print('AVISO: Como las fuentes son de ejemplo recoplidas por internet es posible que fallen y se cierren inesperadamente.')
        print('AVISO: Prueba con otra fuente.')
        print('Cerrando CVAPP...')

    return introducido
