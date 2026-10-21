"""Mide la busqueda por titulo con dos estrategias del TP 2."""

from random import Random
from statistics import median
from time import perf_counter_ns

from busquedas import IndiceTitulosArbol, busqueda_secuencial_por_titulo
from videojuego import Videojuego


TAMANOS = (1_000, 10_000, 100_000)
MUESTRAS = 5
REPETICIONES = 100


def generar_videojuegos(cantidad):
    return [
        Videojuego(
            f"Juego {indice:06d}",
            "Accion",
            "Estudio TP2",
            8.0,
            ["PC"],
        )
        for indice in range(cantidad)
    ]


def preparar_indice_arbol(videojuegos, semilla):
    videojuegos_para_arbol = videojuegos.copy()
    Random(semilla).shuffle(videojuegos_para_arbol)
    return IndiceTitulosArbol(videojuegos_para_arbol)


def medir_busqueda(buscar, titulo):
    mediciones = []

    for _ in range(MUESTRAS):
        inicio = perf_counter_ns()

        for _ in range(REPETICIONES):
            resultado = buscar(titulo)
            if len(resultado) != 1:
                raise AssertionError("La busqueda deberia encontrar un videojuego.")

        mediciones.append((perf_counter_ns() - inicio) / REPETICIONES)

    return median(mediciones) / 1_000_000


def ejecutar_experimento():
    print("N elementos | Secuencial (ms) | Arbol (ms)")
    print("-" * 47)

    for cantidad in TAMANOS:
        videojuegos = generar_videojuegos(cantidad)
        titulo_buscado = videojuegos[-1].nombre
        indice_arbol = preparar_indice_arbol(videojuegos, cantidad)

        tiempo_secuencial = medir_busqueda(
            lambda titulo: busqueda_secuencial_por_titulo(videojuegos, titulo),
            titulo_buscado,
        )
        tiempo_arbol = medir_busqueda(indice_arbol.buscar, titulo_buscado)

        print(
            f"{cantidad:10d} | {tiempo_secuencial:16.4f} | {tiempo_arbol:10.4f}"
        )


if __name__ == "__main__":
    ejecutar_experimento()
