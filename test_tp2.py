import unittest

from busquedas import IndiceTitulosArbol, busqueda_secuencial_por_titulo
from catalogo import CatalogoVideojuegos
from Trabajo_Main import medir_promedio_busqueda
from videojuego import Videojuego


def crear_juego(nombre):
    return Videojuego(nombre, "Accion", "Estudio", 8.0, ["PC"])


class BusquedasTp2Test(unittest.TestCase):
    def setUp(self):
        self.juegos = [
            crear_juego("Zelda"),
            crear_juego("Celeste"),
            crear_juego("Hades"),
        ]

    def test_busqueda_secuencial_encuentra_titulo_sin_distinguir_mayusculas(self):
        resultado = busqueda_secuencial_por_titulo(self.juegos, "cElEsTe")

        self.assertEqual([juego.nombre for juego in resultado], ["Celeste"])

    def test_busqueda_secuencial_no_encuentra_titulo_inexistente(self):
        self.assertEqual(busqueda_secuencial_por_titulo(self.juegos, "Doom"), [])

    def test_arbol_encuentra_titulo_en_ramas_distintas(self):
        indice = IndiceTitulosArbol(self.juegos)

        self.assertEqual([juego.nombre for juego in indice.buscar("ZELDA")], ["Zelda"])
        self.assertEqual([juego.nombre for juego in indice.buscar("Celeste")], ["Celeste"])

    def test_arbol_reune_videojuegos_con_el_mismo_titulo(self):
        indice = IndiceTitulosArbol([crear_juego("Doom"), crear_juego("DOOM")])

        self.assertEqual(len(indice.buscar("doom")), 2)

    def test_catalogo_expone_las_dos_estrategias(self):
        catalogo = CatalogoVideojuegos(self.juegos)

        secuencial = catalogo.buscar_por_titulo_secuencial("Hades")
        arbol = catalogo.buscar_por_titulo_en_arbol("Hades")

        self.assertEqual([juego.nombre for juego in secuencial], ["Hades"])
        self.assertEqual([juego.nombre for juego in arbol], ["Hades"])

    def test_medicion_devuelve_resultado_y_tiempo_positivo(self):
        tiempo, resultados = medir_promedio_busqueda(
            lambda titulo: busqueda_secuencial_por_titulo(self.juegos, titulo),
            "Hades",
            repeticiones=2,
        )

        self.assertGreater(tiempo, 0)
        self.assertEqual([juego.nombre for juego in resultados], ["Hades"])


if __name__ == "__main__":
    unittest.main()
