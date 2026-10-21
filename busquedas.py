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
        self.altura = 1


class IndiceTitulosArbol:
    """Arbol binario de busqueda indexado por el titulo normalizado."""

    def __init__(self, videojuegos=None):
        self._raiz = None
        self._cantidad_titulos = 0

        if videojuegos is not None:
            for videojuego in videojuegos:
                self.agregar(videojuego)

    def _obtener_altura(self, nodo):

        if not nodo:

            return 0
        
        return nodo.altura

    def _obtener_balance(self, nodo):

        if not nodo:

            return 0

        return self._obtener_altura(nodo.izquierdo) - self._obtener_altura(nodo.derecho)

    def _rotar_derecha(self, z):

        y = z.izquierdo
        T3 = y.derecho

        y.derecho = z
        z.izquierdo = T3

        z.altura = 1 + max(self._obtener_altura(z.izquierdo), self._obtener_altura(z.derecho))
        y.altura = 1 + max(self._obtener_altura(y.izquierdo), self._obtener_altura(y.derecho))

        return y # 'y' es la nueva raíz de este sub-árbol

    def _rotar_izquierda(self, z):
        y = z.derecho
        T2 = y.izquierdo

        y.izquierdo = z
        z.derecho = T2

        z.altura = 1 + max(self._obtener_altura(z.izquierdo), self._obtener_altura(z.derecho))
        y.altura = 1 + max(self._obtener_altura(y.izquierdo), self._obtener_altura(y.derecho))

        return y

    def agregar(self, videojuego):

        titulo = normalizar_titulo(videojuego.nombre)

        if titulo == "":

            raise ValueError("El titulo del videojuego no puede estar vacio.")
        
        self._raiz = self._insertar_recursivo(self._raiz, titulo, videojuego)

    def _insertar_recursivo(self, nodo, titulo, videojuego):

        if not nodo:
            self._cantidad_titulos += 1
            return NodoTitulo(titulo, videojuego)

        if titulo == nodo.titulo:
            nodo.videojuegos.append(videojuego)
            return nodo
            
        elif titulo < nodo.titulo:

            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, titulo, videojuego)

        else:

            nodo.derecho = self._insertar_recursivo(nodo.derecho, titulo, videojuego)


        nodo.altura = 1 + max(self._obtener_altura(nodo.izquierdo), self._obtener_altura(nodo.derecho))

        balance = self._obtener_balance(nodo)

        if balance > 1 and titulo < nodo.izquierdo.titulo:

            return self._rotar_derecha(nodo)

        if balance < -1 and titulo > nodo.derecho.titulo:

            return self._rotar_izquierda(nodo)


        if balance > 1 and titulo > nodo.izquierdo.titulo:

            nodo.izquierdo = self._rotar_izquierda(nodo.izquierdo)
            return self._rotar_derecha(nodo)
        
        if balance < -1 and titulo < nodo.derecho.titulo:

            nodo.derecho = self._rotar_derecha(nodo.derecho)
            return self._rotar_izquierda(nodo)

        return nodo

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

    def recorrer_inorden(self):
        """Devuelve los videojuegos ordenados alfabeticamente por titulo."""
        videojuegos = []
        pila = []
        nodo_actual = self._raiz

        while pila or nodo_actual is not None:
            while nodo_actual is not None:
                pila.append(nodo_actual)
                nodo_actual = nodo_actual.izquierdo

            nodo_actual = pila.pop()
            videojuegos.extend(nodo_actual.videojuegos)
            nodo_actual = nodo_actual.derecho

        return videojuegos

    def recorrer_preorden(self):
        """Devuelve los videojuegos visitando raiz, izquierda y derecha."""
        if self._raiz is None:
            return []

        videojuegos = []
        pendientes = [self._raiz]

        while pendientes:
            nodo = pendientes.pop()
            videojuegos.extend(nodo.videojuegos)

            if nodo.derecho is not None:
                pendientes.append(nodo.derecho)
            if nodo.izquierdo is not None:
                pendientes.append(nodo.izquierdo)

        return videojuegos

    def recorrer_postorden(self):
        """Devuelve los videojuegos visitando izquierda, derecha y raiz."""
        if self._raiz is None:
            return []

        videojuegos = []
        pendientes = [(self._raiz, False)]

        while pendientes:
            nodo, visitado = pendientes.pop()

            if visitado:
                videojuegos.extend(nodo.videojuegos)
                continue

            pendientes.append((nodo, True))
            if nodo.derecho is not None:
                pendientes.append((nodo.derecho, False))
            if nodo.izquierdo is not None:
                pendientes.append((nodo.izquierdo, False))

        return videojuegos

    @property
    def cantidad_titulos(self):
        return self._cantidad_titulos