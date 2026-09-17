class Videojuego:
    def __init__(self, nombre, genero, desarrolladora, puntuacion, plataforma):
        self._nombre = nombre
        self._genero = genero
        self._desarrolladora = desarrolladora
        self._puntuacion = puntuacion
        self._plataforma = self._normalizar_plataforma(plataforma)

    @property
    def nombre(self):
        return self._nombre

    @property
    def genero(self):
        return self._genero

    @property
    def desarrolladora(self):
        return self._desarrolladora

    @property
    def puntuacion(self):
        return self._puntuacion

    @property
    def plataforma(self):
        return self._plataforma.copy()

    def pertenece_a_genero(self, genero):
        return self._genero.lower() == genero.lower()

    def esta_en_plataforma(self, plataforma):
        plataforma_buscada = plataforma.lower()
        return any(valor.lower() == plataforma_buscada for valor in self._plataforma)

    def convertir_a_diccionario(self):
        return {
            "nombre": self._nombre,
            "genero": self._genero,
            "desarrolladora": self._desarrolladora,
            "puntuacion": self._puntuacion,
            "plataforma": self._plataforma.copy(),
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["nombre"],
            datos["genero"],
            datos["desarrolladora"],
            datos["puntuacion"],
            datos["plataforma"],
        )

    def __repr__(self):
        plataformas = ", ".join(self._plataforma)
        return (
            f"{self._nombre} | Genero: {self._genero} | "
            f"Desarrolladora: {self._desarrolladora} | "
            f"Puntuacion: {self._puntuacion} | Plataforma: {plataformas}"
        )

    @staticmethod
    def _normalizar_plataforma(plataforma):
        if isinstance(plataforma, list):
            return plataforma

        return [plataforma]
