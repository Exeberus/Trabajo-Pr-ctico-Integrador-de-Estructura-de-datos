"""Pruebas de las propiedades de balance del índice AVL."""

import unittest

from busquedas import IndiceTitulosArbol
from videojuego import Videojuego


def crear_juego(nombre):
    return Videojuego(nombre, "Accion", "Estudio", 8.0, ["PC"])


class ArbolAvlTp4Test(unittest.TestCase):
    def altura_y_validar_balance(self, nodo):
        if nodo is None:
            return 0

        altura_izquierda = self.altura_y_validar_balance(nodo.izquierdo)
        altura_derecha = self.altura_y_validar_balance(nodo.derecho)
        self.assertLessEqual(abs(altura_izquierda - altura_derecha), 1)
        return 1 + max(altura_izquierda, altura_derecha)

    def test_rotaciones_mantienen_balance_para_los_cuatro_casos(self):
        casos = [
            (["C", "B", "A"], "B"),  # izquierda-izquierda
            (["A", "B", "C"], "B"),  # derecha-derecha
            (["C", "A", "B"], "B"),  # izquierda-derecha
            (["A", "C", "B"], "B"),  # derecha-izquierda
        ]

        for titulos, raiz_esperada in casos:
            with self.subTest(titulos=titulos):
                indice = IndiceTitulosArbol(
                    [crear_juego(titulo) for titulo in titulos]
                )
                self.assertEqual(indice._raiz.titulo, raiz_esperada.casefold())
                self.altura_y_validar_balance(indice._raiz)

    def test_insercion_ordenada_conserva_balance_y_busquedas(self):
        videojuegos = [
            crear_juego(f"Juego {numero:04d}") for numero in range(1000)
        ]
        indice = IndiceTitulosArbol(videojuegos)

        self.assertEqual(indice.cantidad_titulos, len(videojuegos))
        self.altura_y_validar_balance(indice._raiz)

        for videojuego in videojuegos:
            self.assertEqual(indice.buscar(videojuego.nombre), [videojuego])

    def test_no_acepta_titulo_vacio(self):
        indice = IndiceTitulosArbol()

        with self.assertRaises(ValueError):
            indice.agregar(crear_juego("   "))


if __name__ == "__main__":
    unittest.main()
