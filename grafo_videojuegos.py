class GrafoVideojuegos:

    def __init__(self):

        self._adyacencia = {}

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