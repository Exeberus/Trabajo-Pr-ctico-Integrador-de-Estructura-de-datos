from busquedas import IndiceTitulosArbol, busqueda_secuencial_por_titulo
from videojuego import Videojuego


class CatalogoVideojuegos:
    def __init__(self, videojuegos=None):
        self._videojuegos = []
        self._indice_por_nombre = {}
        self._indice_por_genero = {}
        self._indice_por_plataforma = {}
        self._indice_titulos_arbol = IndiceTitulosArbol()

        if videojuegos is not None:
            for videojuego in videojuegos:
                self.agregar(videojuego)

    def agregar(self, videojuego):
        if not isinstance(videojuego, Videojuego):
            raise TypeError("Solo se pueden agregar objetos de tipo Videojuego.")

        self._videojuegos.append(videojuego)
        self._agregar_a_indice_nombre(videojuego)
        self._agregar_a_indice_genero(videojuego)
        self._agregar_a_indice_plataforma(videojuego)
        self._indice_titulos_arbol.agregar(videojuego)

    def listar(self):
        return self._videojuegos.copy()

    def buscar_por_nombre(self, texto):
        texto_normalizado = self._normalizar(texto)

        if texto_normalizado in self._indice_por_nombre:
            return [self._indice_por_nombre[texto_normalizado]]

        return [
            videojuego
            for videojuego in self._videojuegos
            if texto_normalizado in self._normalizar(videojuego.nombre)
        ]

    def buscar_por_titulo_secuencial(self, titulo):
        return busqueda_secuencial_por_titulo(self._videojuegos, titulo)

    def buscar_por_titulo_en_arbol(self, titulo):
        return self._indice_titulos_arbol.buscar(titulo)

    def filtrar_por_genero(self, genero):
        clave = self._normalizar(genero)
        return self._indice_por_genero.get(clave, []).copy()

    def filtrar_por_plataforma(self, plataforma):
        clave = self._normalizar(plataforma)
        return self._indice_por_plataforma.get(clave, []).copy()

    def obtener_generos(self):
        return sorted({videojuego.genero for videojuego in self._videojuegos})

    def obtener_plataformas(self):
        plataformas = set()

        for videojuego in self._videojuegos:
            plataformas.update(videojuego.plataforma)

        return sorted(plataformas)

    def top_por_puntuacion(self, limite=10):
        return sorted(
            self._videojuegos,
            key=lambda videojuego: videojuego.puntuacion,
            reverse=True,
        )[:limite]

    def _agregar_a_indice_nombre(self, videojuego):
        clave = self._normalizar(videojuego.nombre)
        self._indice_por_nombre[clave] = videojuego

    def _agregar_a_indice_genero(self, videojuego):
        clave = self._normalizar(videojuego.genero)
        self._indice_por_genero.setdefault(clave, []).append(videojuego)

    def _agregar_a_indice_plataforma(self, videojuego):
        for plataforma in videojuego.plataforma:
            clave = self._normalizar(plataforma)
            self._indice_por_plataforma.setdefault(clave, []).append(videojuego)

    @staticmethod
    def _normalizar(texto):
        return texto.strip().lower()
