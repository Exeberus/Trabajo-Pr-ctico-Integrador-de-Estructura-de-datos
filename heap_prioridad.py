"""Heap binario maximo para priorizar videojuegos por puntuacion."""


class HeapPrioridadVideojuegos:
    """Mantiene arriba el videojuego con mayor puntuacion.

    En caso de empate, conserva primero el videojuego que se agrego antes.
    La prioridad se calcula con la puntuacion disponible en el modelo actual.
    """

    def __init__(self, videojuegos=None):
        self._elementos = []
        self._siguiente_orden = 0

        if videojuegos is not None:
            for videojuego in videojuegos:
                self.insertar(videojuego)

    def insertar(self, videojuego):
        """Agrega un videojuego en O(log n)."""
        prioridad = videojuego.puntuacion
        entrada = (prioridad, self._siguiente_orden, videojuego)
        self._siguiente_orden += 1

        self._elementos.append(entrada)
        self._subir(len(self._elementos) - 1)

    def extraer_maximo(self):
        """Quita y devuelve el videojuego de mayor prioridad."""
        if not self._elementos:
            raise IndexError("No se puede extraer de un heap vacio.")

        self._intercambiar(0, len(self._elementos) - 1)
        entrada_maxima = self._elementos.pop()

        if self._elementos:
            self._bajar(0)

        return entrada_maxima[2]

    def consultar_maximo(self):
        """Devuelve el videojuego de mayor prioridad sin quitarlo."""
        if not self._elementos:
            return None

        return self._elementos[0][2]

    def obtener_top(self, limite=10):
        """Devuelve los primeros N sin modificar el heap original.

        Copiar el arreglo cuesta O(n); extraer N elementos cuesta O(N log n).
        No se vuelve a ordenar el catalogo completo para cada consulta.
        """
        if limite <= 0 or not self._elementos:
            return []

        copia = self._copiar()
        cantidad = min(limite, len(copia._elementos))
        return [copia.extraer_maximo() for _ in range(cantidad)]

    def __len__(self):
        return len(self._elementos)

    def _copiar(self):
        copia = HeapPrioridadVideojuegos()
        copia._elementos = self._elementos.copy()
        copia._siguiente_orden = self._siguiente_orden
        return copia

    def _subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2
            if not self._es_mayor(self._elementos[indice], self._elementos[padre]):
                break

            self._intercambiar(indice, padre)
            indice = padre

    def _bajar(self, indice):
        cantidad = len(self._elementos)

        while True:
            izquierdo = 2 * indice + 1
            derecho = 2 * indice + 2
            mayor = indice

            if izquierdo < cantidad and self._es_mayor(
                self._elementos[izquierdo], self._elementos[mayor]
            ):
                mayor = izquierdo

            if derecho < cantidad and self._es_mayor(
                self._elementos[derecho], self._elementos[mayor]
            ):
                mayor = derecho

            if mayor == indice:
                return

            self._intercambiar(indice, mayor)
            indice = mayor

    @staticmethod
    def _es_mayor(primero, segundo):
        if primero[0] != segundo[0]:
            return primero[0] > segundo[0]

        # En empates, el numero de insercion menor tiene prioridad.
        return primero[1] < segundo[1]

    def _intercambiar(self, primero, segundo):
        self._elementos[primero], self._elementos[segundo] = (
            self._elementos[segundo],
            self._elementos[primero],
        )
