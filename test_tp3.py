import unittest

from busquedas import IndiceTitulosArbol
from catalogo import CatalogoVideojuegos
from videojuego import Videojuego


def crear_juego(nombre):
    return Videojuego(nombre, "Accion", "Estudio", 8.0, ["PC"])


class ArbolTitulosTp3Test(unittest.TestCase):
    def setUp(self):
        self.juegos = [
            crear_juego("Zelda"),
            crear_juego("Celeste"),
            crear_juego("Hades"),
        ]
        self.indice = IndiceTitulosArbol(self.juegos)

    def nombres(self, videojuegos):
        return [juego.nombre for juego in videojuegos]

    def test_recorrido_inorden_esta_ordenado_por_titulo(self):
        self.assertEqual(
            self.nombres(self.indice.recorrer_inorden()),
            ["Celeste", "Hades", "Zelda"],
        )

    def test_recorrido_preorden_visita_raiz_antes_de_sus_hijos(self):
        self.assertEqual(
            self.nombres(self.indice.recorrer_preorden()),
            ["Zelda", "Celeste", "Hades"],
        )

    def test_recorrido_postorden_visita_raiz_al_final(self):
        self.assertEqual(
            self.nombres(self.indice.recorrer_postorden()),
            ["Hades", "Celeste", "Zelda"],
        )

    def test_recorridos_conservan_titulos_duplicados(self):
        indice = IndiceTitulosArbol([crear_juego("Doom"), crear_juego("DOOM")])

        self.assertEqual(self.nombres(indice.recorrer_inorden()), ["Doom", "DOOM"])
        self.assertEqual(self.nombres(indice.recorrer_preorden()), ["Doom", "DOOM"])
        self.assertEqual(self.nombres(indice.recorrer_postorden()), ["Doom", "DOOM"])

    def test_recorridos_de_arbol_vacio_devuelven_lista_vacia(self):
        indice = IndiceTitulosArbol()

        self.assertEqual(indice.recorrer_inorden(), [])
        self.assertEqual(indice.recorrer_preorden(), [])
        self.assertEqual(indice.recorrer_postorden(), [])

    def test_catalogo_integra_los_recorridos_y_valida_el_orden(self):
        catalogo = CatalogoVideojuegos(self.juegos)

        self.assertEqual(
            self.nombres(catalogo.recorrer_titulos("INORDEN")),
            ["Celeste", "Hades", "Zelda"],
        )
        with self.assertRaises(ValueError):
            catalogo.recorrer_titulos("anchura")

    def test_recorrido_iterativo_soporta_arboles_inclinados(self):
        juegos = [crear_juego(f"Juego {indice:04d}") for indice in range(1500)]
        indice = IndiceTitulosArbol(juegos)

        self.assertEqual(indice.recorrer_inorden(), juegos)
        self.assertEqual(indice.recorrer_preorden(), juegos)
        self.assertEqual(indice.recorrer_postorden(), list(reversed(juegos)))


if __name__ == "__main__":
    unittest.main()
