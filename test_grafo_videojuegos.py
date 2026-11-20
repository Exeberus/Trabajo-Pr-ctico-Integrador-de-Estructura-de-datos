import unittest

from grafo_videojuegos import GrafoVideojuegos
from videojuego import Videojuego


def crear_juego(nombre, genero, desarrolladora, plataformas=("PC",)):
    return Videojuego(nombre, genero, desarrolladora, 8.0, list(plataformas))


class GrafoVideojuegosTest(unittest.TestCase):
    def test_relaciones_son_no_dirigidas_y_ordenadas_por_similitud(self):
        origen = crear_juego("Origen", "RPG", "Estudio A", ("PC", "Switch"))
        mismo_genero = crear_juego("Mismo género", "RPG", "Estudio B", ("PC",))
        misma_desarrolladora = crear_juego(
            "Misma desarrolladora", "Puzzle", "Estudio A", ("Switch",)
        )
        solo_plataforma = crear_juego(
            "Solo plataforma", "Estrategia", "Estudio C", ("PC",)
        )
        grafo = GrafoVideojuegos()

        for juego in (origen, mismo_genero, misma_desarrolladora, solo_plataforma):
            grafo.agregar_videojuego(juego)

        relacionados = grafo.relacionados("ORIGEN")
        self.assertEqual(
            [(juego.nombre, puntaje) for juego, puntaje in relacionados],
            [("Mismo género", 4), ("Misma desarrolladora", 3)],
        )
        self.assertEqual(
            [(juego.nombre, puntaje) for juego, puntaje in grafo.relacionados("Mismo género")],
            [("Origen", 4)],
        )
        self.assertEqual(grafo.relacionados("Solo plataforma"), [])

    def test_bfs_devuelve_camino_con_menos_conexiones(self):
        juegos = [
            crear_juego("Inicio", "Aventura", "Estudio A"),
            crear_juego("Puente 1", "RPG", "Estudio A"),
            crear_juego("Puente 2", "RPG", "Estudio B"),
            crear_juego("Destino", "Estrategia", "Estudio B"),
            crear_juego("Atajo", "Aventura", "Estudio B"),
        ]
        grafo = GrafoVideojuegos()

        for juego in juegos:
            grafo.agregar_videojuego(juego)

        self.assertEqual(
            grafo.camino_mas_corto("inicio", "DESTINO"),
            ["Inicio", "Atajo", "Destino"],
        )

    def test_bfs_maneja_extremos_ausentes_aislados_y_iguales(self):
        grafo = GrafoVideojuegos()
        aislado = crear_juego("Aislado", "Puzzle", "Estudio X")
        independiente = crear_juego("Independiente", "Estrategia", "Estudio Y")
        grafo.agregar_videojuego(aislado)
        grafo.agregar_videojuego(independiente)

        self.assertEqual(grafo.camino_mas_corto("ausente", "Aislado"), [])
        self.assertEqual(grafo.camino_mas_corto("Aislado", "ausente"), [])
        self.assertEqual(grafo.camino_mas_corto("Aislado", "Aislado"), ["Aislado"])
        self.assertEqual(grafo.camino_mas_corto("Aislado", "Aislado 2"), [])
        self.assertEqual(grafo.camino_mas_corto("Aislado", "Independiente"), [])

    def test_dfs_visita_todos_los_juegos_alcanzables_una_vez(self):
        juegos = [
            crear_juego("Inicio", "Aventura", "Estudio A"),
            crear_juego("Vecino", "RPG", "Estudio A"),
            crear_juego("Lejano", "RPG", "Estudio B"),
            crear_juego("Aislado", "Puzzle", "Estudio C"),
        ]
        grafo = GrafoVideojuegos()

        for juego in juegos:
            grafo.agregar_videojuego(juego)

        recorrido = grafo.recorrer_profundidad("Inicio")
        self.assertEqual(set(recorrido), {"Inicio", "Vecino", "Lejano"})
        self.assertEqual(len(recorrido), 3)
        self.assertEqual(grafo.recorrer_profundidad("no existe"), [])

    def test_agregar_el_mismo_objeto_no_duplica_vertices(self):
        juego = crear_juego("Único", "Puzzle", "Estudio A")
        grafo = GrafoVideojuegos()

        grafo.agregar_videojuego(juego)
        grafo.agregar_videojuego(juego)

        self.assertEqual(grafo.recorrer_profundidad("Único"), ["Único"])


if __name__ == "__main__":
    unittest.main()
