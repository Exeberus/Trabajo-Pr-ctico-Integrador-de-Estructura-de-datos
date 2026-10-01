"""Estrategias de busqueda por titulo para el TP 2."""


def normalizar_titulo(titulo):
    return titulo.strip().casefold()


def busqueda_secuencial_por_titulo(videojuegos, titulo):
    """Busca todas las coincidencias exactas recorriendo la coleccion."""
    titulo_normalizado = normalizar_titulo(titulo)

    return [
        videojuego
        for videojuego in videojuegos
        if normalizar_titulo(videojuego.nombre) == titulo_normalizado
    ]


class NodoTitulo:
    def __init__(self, titulo, videojuego):
        self.titulo = titulo
        self.videojuegos = [videojuego]
        self.izquierdo = None
        self.derecho = None


class IndiceTitulosArbol:
    """Arbol binario de busqueda indexado por el titulo normalizado."""

    def __init__(self, videojuegos=None):
        self._raiz = None
        self._cantidad_titulos = 0

        if videojuegos is not None:
            for videojuego in videojuegos:
                self.agregar(videojuego)

    def agregar(self, videojuego):
        titulo = normalizar_titulo(videojuego.nombre)

        if titulo == "":
            raise ValueError("El titulo del videojuego no puede estar vacio.")

        if self._raiz is None:
            self._raiz = NodoTitulo(titulo, videojuego)
            self._cantidad_titulos = 1
            return

        nodo_actual = self._raiz

        while True:
            if titulo == nodo_actual.titulo:
                nodo_actual.videojuegos.append(videojuego)
                return

            if titulo < nodo_actual.titulo:
                if nodo_actual.izquierdo is None:
                    nodo_actual.izquierdo = NodoTitulo(titulo, videojuego)
                    self._cantidad_titulos += 1
                    return
                nodo_actual = nodo_actual.izquierdo
            else:
                if nodo_actual.derecho is None:
                    nodo_actual.derecho = NodoTitulo(titulo, videojuego)
                    self._cantidad_titulos += 1
                    return
                nodo_actual = nodo_actual.derecho

    def buscar(self, titulo):
        titulo_normalizado = normalizar_titulo(titulo)
        nodo_actual = self._raiz

        while nodo_actual is not None:
            if titulo_normalizado == nodo_actual.titulo:
                return nodo_actual.videojuegos.copy()

            if titulo_normalizado < nodo_actual.titulo:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_actual = nodo_actual.derecho

        return []

    @property
    def cantidad_titulos(self):
        return self._cantidad_titulos
