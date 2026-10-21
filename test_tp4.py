""" Prueba de AVL """

from time import perf_counter_ns
from videojuego import Videojuego
from busquedas import IndiceTitulosArbol

def test_desbalance():
    print("--- Experimento: Desbalanceo del BST (TP04 - Punto 1) ---")
    
    # 1. Generar 1000 videojuegos con títulos ya ordenados alfabéticamente
    videojuegos_ordenados = []
    for i in range(100):
        # Zfill rellena con ceros para que quede: Juego 000, Juego 001... Juego 999
        titulo = f"Juego {str(i).zfill(3)}"
        juego_falso = Videojuego(titulo, "Test", "TestDev", 10, "PC")
        videojuegos_ordenados.append(juego_falso)

    # 2. Insertarlos en el árbol binario normal
    arbol_desbalanceado = IndiceTitulosArbol()
    for juego in videojuegos_ordenados:
        arbol_desbalanceado.agregar(juego)
        
    print(f"Se insertaron {arbol_desbalanceado.cantidad_titulos} juegos en orden alfabético.")

    # 3. Buscar el último juego (El peor caso posible, quedó en el fondo de la rama derecha)
    titulo_a_buscar = "Juego 999"
    
    # Hacemos varias repeticiones para tener un promedio real de tiempo
    repeticiones = 10_000
    inicio = perf_counter_ns()
    
    for _ in range(repeticiones):
        arbol_desbalanceado.buscar(titulo_a_buscar)
        
    tiempo_total_ns = perf_counter_ns() - inicio
    tiempo_promedio_ms = tiempo_total_ns / repeticiones / 1_000_000

    print(f"Buscando '{titulo_a_buscar}'...")
    print(f"Tiempo promedio de búsqueda (Árbol deformado): {tiempo_promedio_ms:.6f} ms")

if __name__ == "__main__":
    test_desbalance()

## Si el Arbol esta enfermo, demora 0.052484 ms
## Si se aplica AVL al Arbol enfermo, demora 0.000731 ms