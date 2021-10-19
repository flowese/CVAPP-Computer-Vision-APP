from pathlib import Path, PureWindowsPath
import json

# Función que lee archivos json 
def importarjson(fichero):
    with open(fichero, 'r') as fichero:
        fichero = json.load(fichero)
        return fichero


# Función para imprmir un diccionario en terminal
def impdiccionario(fichero):
    fichero = fichero.items() 
    for key, value in list(fichero):
        print(key, '---->', value)


# Tratamiento de rutas para diferentes sistemas operativos
def pathrevision(input):
    filename = PureWindowsPath(input)
    correct_path = Path(filename)
    return correct_path

    
