# Trabajo Practico Integrador de Estructura de Datos

## Integrantes

- Maximo Barraza - DNI 47189012
- Gabriel Avila - DNI 45679295
- Tomas Tagliani - DNI 45480676

## Tema elegido

Videojuegos.

## Objetivo general

Construir un sistema de recomendaciones capaz de almacenar, buscar, ordenar,
relacionar y recomendar videojuegos utilizando estructuras de datos y algoritmos
implementados en Python.

## Entregas realizadas

Esta version inicial cumple con los puntos pedidos para la primera etapa:

- Define la clase principal del dominio: `Videojuego`.
- Implementa encapsulamiento con atributos protegidos y propiedades de solo lectura.
- Separa responsabilidades entre modulos:
  - `videojuego.py`: modelo del dominio.
  - `catalogo.py`: gestion y consultas del catalogo.
  - `datos.py`: carga de datos desde JSON.
  - `Trabajo_Main.py`: interfaz de terminal.
- Carga datos de prueba desde `datos/videojuegos.json`.
- Incluye una interfaz de terminal.
- Implementa operaciones utiles:
  - Listar videojuegos.
  - Buscar por nombre.
  - Filtrar por genero.
  - Filtrar por plataforma.
  - Explorar categorias.
  - Mostrar top por puntuacion.

### TP 2 - Analisis de algoritmos

- Compara la busqueda por titulo exacto con dos estrategias: recorrido
  secuencial y arbol binario de busqueda.
- Incorpora `busquedas.py`, que contiene ambas implementaciones.
- Permite elegir la estrategia desde la opcion de busqueda del menu.
- Incluye `experimento_tp2.py` para generar mediciones reproducibles con
  1.000, 10.000 y 100.000 videojuegos.
- Incluye [el analisis completo](ANALISIS_TP2.md) con la tabla de resultados,
  complejidades y conclusion tecnica.

## Como ejecutar

Desde la carpeta del proyecto:

```bash
python Trabajo_Main.py
```

Para ejecutar las mediciones del TP 2:

```bash
python experimento_tp2.py
```

La opcion 7 del menu mide las dos estrategias sobre los videojuegos reales
cargados desde el archivo JSON. Repite cada consulta 10.000 veces y muestra el
tiempo promedio para poder hacer una demostracion en vivo.

Para ejecutar las pruebas:

```bash
python -m unittest -v
```

## Estructura del proyecto

```text
.
├── Trabajo_Main.py
├── catalogo.py
├── busquedas.py
├── datos.py
├── videojuego.py
├── experimento_tp2.py
├── test_tp2.py
├── ANALISIS_TP2.md
├── datos/
│   └── videojuegos.json
├── Objetivos.txt
└── UML Tp Estructura de Datos.png
```

## Proximas etapas

El proyecto esta preparado para incorporar las estructuras de datos pedidas en
las siguientes entregas:

- Heap para rankings y prioridades.
- Grafos para relaciones entre videojuegos.
- BFS/DFS y caminos minimos para recomendaciones y conexiones entre juegos.
