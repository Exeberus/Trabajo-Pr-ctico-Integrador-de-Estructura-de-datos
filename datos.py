import json

from videojuego import Videojuego


def cargar_videojuegos_desde_json(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return [Videojuego.desde_diccionario(item) for item in datos]
