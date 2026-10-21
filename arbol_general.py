class NodoCategoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []
        self.videojuegos = [] 

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def contar_total_videojuegos(self):
        # Cuenta sus propios juegos + los juegos de todos sus hijos
        total = len(self.videojuegos)
        for hijo in self.hijos:
            total += hijo.contar_total_videojuegos()
        return total


class ArbolCategorias:
    def __init__(self, categoria_raiz="Videojuegos"):
        self.raiz = NodoCategoria(categoria_raiz)

    def buscar_categoria(self, nodo_actual, nombre_buscado):
        if nodo_actual.nombre.lower() == nombre_buscado.lower():
            return nodo_actual
        
        for hijo in nodo_actual.hijos:
            resultado = self.buscar_categoria(hijo, nombre_buscado)
            if resultado is not None:
                return resultado
                
        return None

    def agregar_categoria(self, nombre_padre, nombre_nueva_categoria):
        nodo_padre = self.buscar_categoria(self.raiz, nombre_padre)
        if nodo_padre is None:
            raise ValueError(f"La categoria padre '{nombre_padre}' no existe.")
        
        nuevo_nodo = NodoCategoria(nombre_nueva_categoria)
        nodo_padre.agregar_hijo(nuevo_nodo)
        return nuevo_nodo

    def recorrer_y_mostrar(self, nodo, nivel=0):
        sangria = "    " * nivel
        # Ahora usamos el contador recursivo en lugar del len() de la lista vacía
        total_juegos = nodo.contar_total_videojuegos()
        print(f"{sangria}├── {nodo.nombre} ({total_juegos} juegos)")
        
        for hijo in nodo.hijos:
            self.recorrer_y_mostrar(hijo, nivel + 1)