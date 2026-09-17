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

## Entrega actual: TP 1 - Objetos y clases

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

## Como ejecutar

Desde la carpeta del proyecto:

```bash
python Trabajo_Main.py
```

## Estructura del proyecto

```text
.
├── Trabajo_Main.py
├── catalogo.py
├── datos.py
├── videojuego.py
├── datos/
│   └── videojuegos.json
├── Objetivos.txt
└── UML Tp Estructura de Datos.png
```

## Proximas etapas

El proyecto esta preparado para incorporar las estructuras de datos pedidas en
las siguientes entregas:

- Arboles para busquedas eficientes.
- Heap para rankings y prioridades.
- Grafos para relaciones entre videojuegos.
- BFS/DFS y caminos minimos para recomendaciones y conexiones entre juegos.
