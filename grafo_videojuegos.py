from collections import deque

class GrafoVideojuegos:

    def __init__(self):

        self._adyacencia = {}

    def _buscar_videojuego(self, nombre):

        nombre_buscado = self._normalizar(nombre)

        for videojuego in self._adyacencia:

            if self._normalizar(videojuego.nombre) == nombre_buscado:
                return videojuego

        return None

    def camino_mas_corto(self, origen, destino):

        videojuego_origen = self._buscar_videojuego(origen)
        videojuego_destino = self._buscar_videojuego(destino)

        # Comprobar que ambos videojuegos existan
        if videojuego_origen is None or videojuego_destino is None:
            return []

        # Inicializar estructuras
        cola = deque([videojuego_origen])

        visitados = {videojuego_origen}

        padres = {videojuego_origen: None}

        # Recorrido BFS
        while cola:

            actual = cola.popleft()

            # Comprobar si encontramos el destino
            if actual == videojuego_destino:

                camino = []
                actual = videojuego_destino

                # Reconstruir el camino utilizando los padres
                while actual is not None:
                    camino.append(actual.nombre)
                    actual = padres[actual]

                return camino[::-1]

            # Explorar los vecinos
            for vecino in self._adyacencia[actual]:

                if vecino not in visitados:

                    visitados.add(vecino)

                    padres[vecino] = actual

                    cola.append(vecino)

        # No existe un camino entre ambos videojuegos
        return []

    def recorrer_profundidad(self, origen):

        videojuego_origen = self._buscar_videojuego(origen)

        # Comprobar que el videojuego exista
        if videojuego_origen is None:
            return []

        # Inicializar estructuras
        pila = [videojuego_origen]

        visitados = {videojuego_origen}

        recorrido = []

        # Recorrido DFS
        while pila:

            actual = pila.pop()

            recorrido.append(actual.nombre)

            # Obtener los vecinos en orden inverso
            vecinos = list(self._adyacencia[actual].keys())

            for vecino in reversed(vecinos):

                if vecino not in visitados:

                    visitados.add(vecino)

                    pila.append(vecino)

        return recorrido

    def agregar_videojuego(self, videojuego):

        if videojuego in self._adyacencia:
            return

        self._adyacencia[videojuego] = {}

        for existente in list(self._adyacencia):

            if existente is videojuego:
                continue

            puntaje = self._calcular_similitud(videojuego, existente)

            mismo_genero = (
                self._normalizar(videojuego.genero)
                == self._normalizar(existente.genero)
            )
            misma_desarrolladora = (
                self._normalizar(videojuego.desarrolladora)
                == self._normalizar(existente.desarrolladora)
            )

            if mismo_genero or misma_desarrolladora:

                self._adyacencia[videojuego][existente] = puntaje
                self._adyacencia[existente][videojuego] = puntaje

    def relacionados(self, nombre):

        nombre_buscado = self._normalizar(nombre)

        for videojuego, vecinos in self._adyacencia.items():

            if self._normalizar(videojuego.nombre) == nombre_buscado:

                return sorted(

                    vecinos.items(),
                    key=lambda relacion: relacion[1],
                    reverse=True,

                )

        return []

    @staticmethod
    def _calcular_similitud(juego_a, juego_b):
        puntaje = 0

        if (
            
            GrafoVideojuegos._normalizar(juego_a.genero)
            == GrafoVideojuegos._normalizar(juego_b.genero)
        ):
            puntaje += 3

        if (

            GrafoVideojuegos._normalizar(juego_a.desarrolladora)
            == GrafoVideojuegos._normalizar(juego_b.desarrolladora)
        ):
            puntaje += 2

        plataformas_a = {

            GrafoVideojuegos._normalizar(plataforma)
            for plataforma in juego_a.plataforma
        }
        plataformas_b = {

            GrafoVideojuegos._normalizar(plataforma)
            for plataforma in juego_b.plataforma
        }

        puntaje += len(plataformas_a & plataformas_b)
        return puntaje

    @staticmethod
    def _normalizar(texto):
        return texto.strip().lower()

    def recorrer_profundidad(self, origen):

        videojuego_origen = self._buscar_videojuego(origen)

        if videojuego_origen is None:
            return []

        pila = [videojuego_origen]

        visitados = {videojuego_origen}

        recorrido = []

        while pila:

            actual = pila.pop()

            recorrido.append(actual.nombre)

            vecinos = list(self._adyacencia[actual].keys())

            for vecino in reversed(vecinos):

                if vecino not in visitados:

                    visitados.add(vecino)

                    pila.append(vecino)

        return recorrido