# Trabajo Práctico Integrador — Sistema de recomendaciones de videojuegos

Sistema de terminal para guardar, buscar, explorar, relacionar y recomendar videojuegos. El proyecto usa clases del dominio y estructuras de datos implementadas en Python para resolver consultas concretas.

## Integrantes

- Maximo Barraza
- Gabriel Avila
- Tomas Tagliani

## Alcance

La rama integra los avances de TP0 a TP8. El TP9 fue salteado por decisión de la cátedra; el recorrido entre juegos de esta versión es BFS y busca el camino con menor cantidad de conexiones. No calcula caminos de costo mínimo según los puntajes de similitud. TP10 corresponde a la integración y defensa final.

El catálogo de ejemplo contiene 12 videojuegos en `datos/videojuegos.json`. El equipo puede ampliar ese archivo manteniendo los campos del modelo.

## Funcionalidades

- Listar videojuegos.
- Buscar por título exacto con búsqueda secuencial o con el índice AVL.
- Filtrar por género o plataforma.
- Explorar categorías mediante un árbol general.
- Mostrar los videojuegos con mayor puntuación usando una heap binaria máxima propia.
- Comparar la búsqueda secuencial con la búsqueda AVL.
- Recorrer el índice de títulos en inorden, preorden o postorden.
- Ver videojuegos relacionados, ordenados por puntaje de similitud.
- Buscar un camino con menos conexiones mediante BFS.
- Explorar las conexiones alcanzables mediante DFS.

## Estructuras y complejidad

- **Índice AVL de títulos** (`busquedas.py`): inserción y búsqueda en O(log n) en el peor caso; la búsqueda secuencial cuesta O(n). Los títulos normalizados iguales comparten un nodo.
- **Heap binaria máxima** (`heap_prioridad.py`): insertar y extraer el máximo cuestan O(log n); consultar el máximo cuesta O(1). `obtener_top(k)` copia el arreglo del heap y extrae hasta k elementos, por lo que cuesta O(n + k log n) y deja intacto el heap del catálogo.
- **Árbol general de categorías** (`arbol_general.py`): organiza categorías y videojuegos para la opción de exploración.
- **Grafo no dirigido** (`grafo_videojuegos.py`): conecta juegos que comparten género o desarrolladora. El puntaje de similitud suma género, desarrolladora y plataformas compartidas. BFS y DFS recorren en O(V + E); la búsqueda del videojuego por nombre también recorre los vértices.
- **Índices del catálogo** (`catalogo.py`): agrupan los juegos por género y plataforma para facilitar los filtros.

## Requisitos

- Python 3.8 o posterior.
- No requiere paquetes externos; usa la biblioteca estándar de Python.

## Ejecución

Desde la carpeta del repositorio:

```bash
python Trabajo_Main.py
```

## Pruebas automatizadas

Ejecutar desde la carpeta del repositorio:

```bash
python -m unittest discover -v
```

Las pruebas cubren búsquedas y recorridos del AVL, equilibrio del árbol, operaciones y conservación del heap, integración del Top del catálogo y consultas del grafo con BFS y DFS.

## Estructura del repositorio

```text
.
├── Trabajo_Main.py
├── videojuego.py
├── catalogo.py
├── datos.py
├── busquedas.py
├── arbol_general.py
├── heap_prioridad.py
├── grafo_videojuegos.py
├── Proyecto.zip
├── datos/
│   └── videojuegos.json
├── ANALISIS_TP2.md
├── ANALISIS_TP3.md
├── experimento_tp2.py
├── test_tp2.py
├── test_tp3.py
├── test_tp4.py
├── test_heap_prioridad.py
└── test_grafo_videojuegos.py
```

El repositorio conserva `Proyecto.zip` como adjunto; los archivos fuente actuales están en la raíz y en las carpetas listadas arriba.

## Documentación disponible

- [Análisis del TP2](ANALISIS_TP2.md)
- [Análisis del TP3](ANALISIS_TP3.md)
- [Objetivos del proyecto](Objetivos.txt)
- [Diagrama UML](UML%20Tp%20Estructura%20de%20Datos.png)

## Uso del código

Las estructuras y algoritmos principales se implementan dentro del proyecto. Se usan módulos estándar como `json`, `pathlib` y `collections.deque` para carga de datos y operaciones auxiliares.
