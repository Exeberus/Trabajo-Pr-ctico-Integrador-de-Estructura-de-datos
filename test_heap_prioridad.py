import unittest

from catalogo import CatalogoVideojuegos
from heap_prioridad import HeapPrioridadVideojuegos
from videojuego import Videojuego


def crear_juego(nombre, puntuacion):
    return Videojuego(nombre, "Accion", "Estudio", puntuacion, ["PC"])


class HeapPrioridadVideojuegosTest(unittest.TestCase):
    def test_consulta_y_extraccion_respetan_maximo_y_desempate_estable(self):
        juegos = [
            crear_juego("Primero", 9),
            crear_juego("Mayor", 10),
            crear_juego("Segundo", 9),
        ]
        heap = HeapPrioridadVideojuegos(juegos)

        self.assertIs(heap.consultar_maximo(), juegos[1])
        self.assertEqual(
            [heap.extraer_maximo(), heap.extraer_maximo(), heap.extraer_maximo()],
            [juegos[1], juegos[0], juegos[2]],
        )
        self.assertEqual(len(heap), 0)

    def test_obtener_top_no_modifica_heap_original(self):
        juegos = [
            crear_juego("A", 7),
            crear_juego("B", 10),
            crear_juego("C", 8),
        ]
        heap = HeapPrioridadVideojuegos(juegos)

        self.assertEqual(
            [juego.nombre for juego in heap.obtener_top(2)],
            ["B", "C"],
        )
        self.assertEqual(len(heap), 3)
        self.assertIs(heap.consultar_maximo(), juegos[1])

    def test_limites_de_top(self):
        heap = HeapPrioridadVideojuegos(
            [crear_juego("A", 7), crear_juego("B", 10)]
        )

        self.assertEqual(heap.obtener_top(0), [])
        self.assertEqual(heap.obtener_top(-1), [])
        self.assertEqual(
            [juego.nombre for juego in heap.obtener_top(10)],
            ["B", "A"],
        )

    def test_extraer_de_heap_vacio_falla_con_error_claro(self):
        with self.assertRaises(IndexError):
            HeapPrioridadVideojuegos().extraer_maximo()

    def test_catalogo_usa_heap_para_el_top(self):
        juegos = [
            crear_juego("A", 7),
            crear_juego("B", 10),
            crear_juego("C", 8),
        ]
        catalogo = CatalogoVideojuegos(juegos)

        self.assertEqual(
            [juego.nombre for juego in catalogo.top_por_puntuacion(2)],
            ["B", "C"],
        )


if __name__ == "__main__":
    unittest.main()
