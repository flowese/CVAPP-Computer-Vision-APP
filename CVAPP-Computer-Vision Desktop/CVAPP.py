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
# Computer Vision APP
# Creado por @flowese versión: 1.7 para terminal.
# Reconocimiento de objetos en tiempo real para fuentes de video.
# Fichero: main.py
# ---> Pendiente implementar detector de género y de cara en #GESTIÓN DE MEDIOS*

# LIBRERÍAS
from imutils.video import FileVideoStream  # Gestión de video
import numpy as np  # Soporte vectores y matrices
import imutils
import cv2
import time
import os, random
from cvlib.object_detection import draw_bbox  # Detección de objetos
import cvlib as cv  # Detección de objetos
from inputimeout import inputimeout, TimeoutOccurred
# Funciones de estilos en fichero estilos.py
from config.estilos import convertoasci, mostrar_cargando, imprtextos, limpiarterminal
# Funciones generales en fichero funciones.py
from config.funciones import importarjson, impdiccionario, pathrevision

# ANIMACIONES DE LANZAMIENTO

# - Limpiar terminal antes de ejecutar la app
limpiarterminal()
# - Mensajes de inicio
titulo_inicio = convertoasci("Computer Vision APP v 1.7t")
print(titulo_inicio)
# Funcion imprime texto inicio
imprtextos('inicio')

# - Barra de animación de carga
mostrar_cargando()
# Espera 0.5 y limpia la pantalla después de la intro.
print("\nInicio completado.")
limpiarterminal()

# - Imprime ASCI art el título orígenes
titulo_origenes = convertoasci("ORIGENES")
print(titulo_origenes)

print('~ Las fuentes son de internet y no está garantizado que funcionen siempre. \n')

# - Funcion que imprime todos los nombres del diccionario origenes
source_origenes = 'config\\origenes.json'
# - Funcion reconocimiento del path de archivos en windows, mac o linux
tratamientopath = pathrevision(source_origenes)
origenes = importarjson(tratamientopath)
impdiccionario(origenes)

# - Input por terminal al usuario definiendo el origen (con timeout)
# - Si no se introduce input por defecto selecciona uno aleatorio.

try:
    origen_def = inputimeout(
        prompt='\nEscribe el NOMBRE del orígen: ', timeout=10)
    while origen_def != origenes: 
        if origen_def in origenes:
            limpiarterminal()
            print('\n\nOrígen seleccionado: ', origen_def, '\n\n')
            time.sleep(2)
            # - Lee del diccionario de orígenes con el seleccionado
            origen_in = origenes[origen_def]
            time.sleep(1)
            limpiarterminal()
            break
        else:
            limpiarterminal()
            print(titulo_origenes)
            print('~ Las fuentes son de internet y no está garantizado que funcionen siempre. \n')
            impdiccionario(origenes)
            print ('\nERROR: El nombre que has introducido no existe en la lista de orígenes.')
            origen_def = inputimeout(
                prompt='\nEscribe el NOMBRE del orígen: ', timeout=10)

except TimeoutOccurred:
    origen_def = random.choice(list(origenes.keys())) # Para obtener un valor key random del diccionario origenes
    origen_in = origenes[origen_def]
    print('\n\n---> AL no intriducir ningún valor se ha seleccionado automáticamente', origen_def+'.')    
    time.sleep(3)
    limpiarterminal()

# - Imprime ASCI art el título modelo
titulo_modelo = convertoasci("MODELO DE I.A.")
print(titulo_modelo)
# Funcion imprime texto de modelo
imprtextos('modelo')
list(origenes)
# - Imprime todos los nombre del diccionario de modelos

# - Funcion que imprime todos los nombres del diccionario modelos
source_modelos = 'config\\modelos.json'
# - Funcion reconocimiento del path de archivos en windows, mac o linux
tratamientopath = pathrevision(source_modelos)
modelos = importarjson(tratamientopath)
impdiccionario(modelos)


# - Input por terminal al usuario definiendo el modelo de yolo (con timeout)
try:
    modelo_def = inputimeout(
        prompt='\nEscribe el NOMBRE del modelo: ', timeout=3)
    if not modelo_def:
        modelo_def = 'Preciso'
except TimeoutOccurred:
    modelo_def = 'Preciso'
    print('\n--> No se ha introducido un valor. Selección automática activada.')
time.sleep(1)

# - Lee el origen de datos definido por el input de usuario anterior
modelo_in = modelos[modelo_def]
# - Comprueba el modelo seleccionado e imprime la advertencia describiendo el modelo
print('\n·Modelo de computación seleccionado:', modelo_def)
if modelo_def == 'Rapido':
    print('~ Recuerda que este modelo es más rápido pero menos preciso.')
else:
    print('~ Recuerda que este modelo es más lento pero más preciso.')


# FORMATOS DE ESTILO EN PANTALLA
tipofuente = cv2.FONT_HERSHEY_SIMPLEX
tamanofuente = 0.8
grosorfuente = 1
# - Autos
colorfuente_coches = 0, 0, 255  # BRG
postexto_coches = 40, 50

colorfuente_camiones = 0, 0, 255  # BRG
postexto_camiones = 40, 80
# - Humanos
colorfuente_personas = 255, 0, 0  # BRG
postexto_personas = 40, 120

## Aún no implementada la funión.
colorfuente_hombres = 255, 0, 0  # BRG
postexto_hombres = 40, 160
## Aún no implementada la funión.
colorfuente_mujeres = 255, 0, 0  # BRG
postexto_mujeres = 40, 200

# GESTIÓN DE MEDIOS
# Iniciando fuente de video
fvs = FileVideoStream(origen_in).start()
print('\nProcesando fuente multimedia...')
time.sleep(1)
print('\nMostrando visualizador...\n')

# - Gestionando el video frame a frame
while fvs.more():
    # - Leer fuente de video
    videoproceso = fvs.read()
    # - Reajuste de tamano
    videoproceso = imutils.resize(videoproceso, width=1280)
    # - Conversión de color a blanco y negro
    videoproceso = cv2.cvtColor(videoproceso, cv2.COLOR_BGR2GRAY)
    # - Matriz
    videoproceso = np.dstack([videoproceso, videoproceso, videoproceso])

    # DETECTORES DE VISIÓN POR COMPUTADORA
    # - Detector de objetos
    bbox, label, conf = cv.detect_common_objects(videoproceso, model=modelo_in)

    # - Detector de rostros
    #faces, confidences = cv.detect_face(videoproceso)
    # - Detector de género
    #label, confidence = cv.detect_gender(videoproceso)

    # - Limpiar pantalla del terminal en cada frame
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

    # - Mensajes de consola en captura
    titulo_capturando = convertoasci("Computer Vision APP v 1.7t")
    print(titulo_capturando)
    # Funcion imprime texto de consola
    imprtextos('consola')
    print('·Modelo:', modelo_def, '  ·Fuente:', origen_def, ' \n')
    print('Para cerrar la ventana de visualización pulsando la tecla "Q" o con "Control+C en el terminal."')

    # Procesado del display layout
    out = draw_bbox(videoproceso, bbox, label, conf)

    # CONTADORES EN PANTALLA STREAM
    # - Contador Personas
    out = cv2.putText(videoproceso, 'Coches: '+str(label.count('car')), (postexto_coches),
                      tipofuente, tamanofuente, (colorfuente_coches), grosorfuente, cv2.LINE_AA)
    # - Contador Camiones
    out = cv2.putText(videoproceso, 'Camiones: '+str(label.count('truck')), (postexto_camiones),
                      tipofuente, tamanofuente, (colorfuente_camiones), grosorfuente, cv2.LINE_AA)
    # - Contador Personas
    out = cv2.putText(videoproceso, 'Personas: '+str(label.count('person')), (postexto_personas),
                      tipofuente, tamanofuente, (colorfuente_personas), grosorfuente, cv2.LINE_AA)

    # Pendiente implementar - Detección de género
    #out = cv2.putText(videoproceso,'Hombres: '+str(label.count('male')),(postexto_hombres),tipofuente,tamanofuente,(colorfuente_hombres),grosorfuente,cv2.LINE_AA)
    #out = cv2.putText(videoproceso,'Mujeres: '+str(label.count('female')),(postexto_mujeres),tipofuente,tamanofuente,(colorfuente_mujeres),grosorfuente,cv2.LINE_AA)

    cv2.imshow('(CVAPP) Computer Vision APP {origen_def} - Powered by @flowese',
               out)  # Título de la ventana
    if cv2.waitKey(10) & 0xFF == ord('q'):  # Pulsar tecla Q para salir
        break

# CERRAR VENTANAS
imprtextos('final')

cv2.destroyAllWindows()


