### Comienzo del Proyecto

class Videojuego() :

    def __init__(self, Nombre, Genero, Desarrolladora, Puntuacion, Plataforma):
        self.nombre = Nombre
        self.genero = Genero
        self.desarrolladora = Desarrolladora
        self.puntuacion = Puntuacion
        self.plataforma = Plataforma

        pass

    def nombrar_juego(self):
        print(self.nombre)

juego = Videojuego("Zelda", "Action Rpg", "Nintendo", 100, ["Nintendo Switch", "Nintendo Switch 2"])
juego.nombrar_juego()