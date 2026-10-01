from pathlib import Path
from time import perf_counter_ns

from catalogo import CatalogoVideojuegos
from datos import cargar_videojuegos_desde_json


RUTA_DATOS = Path(__file__).parent / "datos" / "videojuegos.json"
REPETICIONES_MEDICION = 10_000


def mostrar_juegos(videojuegos):
    if not videojuegos:
        print("No se encontraron videojuegos.")
        return

    for indice, juego in enumerate(videojuegos, start=1):
        print(f"{indice}. {juego}")


def pedir_texto(mensaje):
    return input(mensaje).strip()


def pedir_entero(mensaje, valor_por_defecto):
    texto = input(mensaje).strip()

    if texto == "":
        return valor_por_defecto

    if not texto.isdigit():
        print(f"Valor invalido. Se usara {valor_por_defecto}.")
        return valor_por_defecto

    return int(texto)


def listar_juegos(catalogo):
    print("\n--- Lista de videojuegos ---")
    mostrar_juegos(catalogo.listar())


def buscar_juego(catalogo):
    nombre = pedir_texto("\nIngrese el titulo exacto: ")
    estrategia = pedir_texto("Estrategia [1: secuencial, 2: arbol] [1]: ")

    if estrategia == "2":
        resultados = catalogo.buscar_por_titulo_en_arbol(nombre)
        nombre_estrategia = "busqueda en arbol"
    else:
        resultados = catalogo.buscar_por_titulo_secuencial(nombre)
        nombre_estrategia = "busqueda secuencial"

    print(f"\n--- Resultado de {nombre_estrategia} ---")
    mostrar_juegos(resultados)


def medir_promedio_busqueda(buscar, titulo, repeticiones=REPETICIONES_MEDICION):
    for _ in range(100):
        buscar(titulo)

    inicio = perf_counter_ns()

    for _ in range(repeticiones):
        resultados = buscar(titulo)

    tiempo_total_ns = perf_counter_ns() - inicio
    tiempo_promedio_ms = tiempo_total_ns / repeticiones / 1_000_000
    return tiempo_promedio_ms, resultados


def comparar_busquedas(catalogo):
    titulo = pedir_texto("\nIngrese el titulo exacto a medir: ")
    tiempo_secuencial, resultados_secuencial = medir_promedio_busqueda(
        catalogo.buscar_por_titulo_secuencial,
        titulo,
    )
    tiempo_arbol, resultados_arbol = medir_promedio_busqueda(
        catalogo.buscar_por_titulo_en_arbol,
        titulo,
    )

    nombres_secuencial = [juego.nombre for juego in resultados_secuencial]
    nombres_arbol = [juego.nombre for juego in resultados_arbol]

    print("\n--- Comparacion sobre el catalogo actual ---")
    print(f"Videojuegos cargados: {len(catalogo.listar())}")
    print(f"Consultas por estrategia: {REPETICIONES_MEDICION}")
    print(f"Secuencial: {tiempo_secuencial:.6f} ms por busqueda")
    print(f"Arbol: {tiempo_arbol:.6f} ms por busqueda")
    print(f"Resultados coinciden: {'si' if nombres_secuencial == nombres_arbol else 'no'}")


def filtrar_por_genero(catalogo):
    genero = pedir_texto("\nIngrese el genero: ")
    resultados = catalogo.filtrar_por_genero(genero)

    print("\n--- Juegos del genero indicado ---")
    mostrar_juegos(resultados)


def filtrar_por_plataforma(catalogo):
    plataforma = pedir_texto("\nIngrese la plataforma: ")
    resultados = catalogo.filtrar_por_plataforma(plataforma)

    print("\n--- Juegos de la plataforma indicada ---")
    mostrar_juegos(resultados)


def explorar_categorias(catalogo):
    print("\n--- Generos disponibles ---")
    for genero in catalogo.obtener_generos():
        cantidad = len(catalogo.filtrar_por_genero(genero))
        print(f"- {genero} ({cantidad} juegos)")

    print("\n--- Plataformas disponibles ---")
    for plataforma in catalogo.obtener_plataformas():
        cantidad = len(catalogo.filtrar_por_plataforma(plataforma))
        print(f"- {plataforma} ({cantidad} juegos)")


def mostrar_top(catalogo):
    limite = pedir_entero("\nCantidad a mostrar [10]: ", 10)
    resultados = catalogo.top_por_puntuacion(limite)

    print(f"\n--- Top {limite} videojuegos por puntuacion ---")
    mostrar_juegos(resultados)


def mostrar_menu():
    print("\n==============================")
    print("   SISTEMA DE VIDEOJUEGOS")
    print("==============================")
    print("1. Listar videojuegos")
    print("2. Buscar videojuego")
    print("3. Filtrar por genero")
    print("4. Filtrar por plataforma")
    print("5. Explorar categorias")
    print("6. Top por puntuacion")
    print("7. Comparar tiempos de busqueda")
    print("0. Salir")


def ejecutar_terminal():
    videojuegos = cargar_videojuegos_desde_json(RUTA_DATOS)
    catalogo = CatalogoVideojuegos(videojuegos)

    opciones = {
        "1": listar_juegos,
        "2": buscar_juego,
        "3": filtrar_por_genero,
        "4": filtrar_por_plataforma,
        "5": explorar_categorias,
        "6": mostrar_top,
        "7": comparar_busquedas,
    }

    while True:
        mostrar_menu()
        opcion = pedir_texto("Seleccione una opcion: ")

        if opcion == "0":
            print("Gracias por usar el sistema.")
            break

        accion = opciones.get(opcion)

        if accion is None:
            print("Opcion invalida. Intente nuevamente.")
            continue

        accion(catalogo)


if __name__ == "__main__":
    ejecutar_terminal()
