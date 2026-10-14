# TP 3 - Arbol binario de busqueda

## Necesidad y clave de ordenamiento

El catalogo necesita buscar videojuegos por titulo exacto y mostrar sus
coincidencias. El indice se ordena por el titulo normalizado con `strip()` y
`casefold()`, para que las consultas no distingan mayusculas ni espacios
exteriores. Si hay titulos iguales despues de normalizar, el nodo conserva
todas las instancias en orden de insercion.

## Operaciones

`IndiceTitulosArbol` implementa la insercion y la busqueda iterativamente. La
interfaz del catalogo permite elegir busqueda secuencial o por arbol, comparar
ambas estrategias y recorrer el indice en inorden, preorden o postorden. El
inorden presenta los videojuegos ordenados alfabeticamente por titulo; los
otros recorridos muestran el orden estructural del arbol.

## Complejidad

Sea `h` la altura del arbol y `n` la cantidad de titulos distintos.

| Operacion | Arbol binario de busqueda |
| --- | --- |
| Insercion | O(h) |
| Busqueda | O(h) |
| Inorden, preorden o postorden | O(n + m), siendo `m` la cantidad de videojuegos devueltos |

Con inserciones de orden aleatorio, la altura esperada es O(log n). Si se
insertan titulos ordenados, el arbol puede inclinarse y la insercion y busqueda
llegan a O(n). Los recorridos visitan cada nodo una vez. El arbol de esta etapa
no se auto-balancea; esa garantia corresponde al AVL de la etapa siguiente.

## Comparacion con la busqueda secuencial del TP 2

La opcion 7 de la aplicacion mide las busquedas sobre los datos reales del
catalogo. `experimento_tp2.py` conserva la comparacion reproducible del TP 2
con colecciones sinteticas de 1.000, 10.000 y 100.000 elementos, cinco muestras
y mediana. El arbol se construye antes de medir, por lo que estos valores
comparan consultas repetidas y no incluyen el costo inicial de construir el
indice. La busqueda secuencial cuesta O(n); la del arbol cuesta O(h), que es
O(log n) esperado si la altura se mantiene baja y O(n) en el peor caso.

Ejecucion local de `python experimento_tp2.py`:

| Videojuegos | Secuencial (ms por busqueda) | Arbol (ms por busqueda) |
| ---: | ---: | ---: |
| 1.000 | 0,1748 | 0,0008 |
| 10.000 | 1,7377 | 0,0008 |
| 100.000 | 18,3707 | 0,0013 |

En esta ejecucion, al multiplicar por 100 la coleccion, la busqueda secuencial
tardo cerca de 105 veces mas; la del arbol se mantuvo en el mismo orden de
magnitud. Son tiempos orientativos de una unica maquina, no garantias.

Para interpretar la medicion en la aplicacion, considerar que la carga inicial
del catalogo tambien construye el arbol. Conviene reutilizar el indice para
muchas consultas; para una sola consulta sobre una coleccion chica, el costo de
construccion puede no compensar. Los tiempos concretos dependen de la maquina y
se deben leer de la ejecucion local de `python experimento_tp2.py`.

## Pruebas

`test_tp3.py` verifica insercion indirectamente mediante los recorridos,
ordenamiento, los tres ordenes de visita, titulos duplicados, arbol vacio,
validacion del catalogo y un arbol inclinado de 1.500 nodos. Ejecutar junto con
las pruebas anteriores mediante:

```bash
python -m unittest -v
```
