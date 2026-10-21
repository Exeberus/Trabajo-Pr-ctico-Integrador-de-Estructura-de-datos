# TP 2 - Analisis de algoritmos

## Operacion elegida

Se comparo la busqueda de un videojuego por titulo exacto, sin distinguir
mayusculas de minusculas. Es una operacion critica del catalogo porque se usa
para encontrar rapidamente un juego antes de mostrar o procesar sus datos.

## Estrategias implementadas

1. Busqueda secuencial: recorre la lista completa y compara el titulo de cada
   videojuego con el titulo solicitado.
2. Busqueda en arbol: guarda los titulos en un arbol binario de busqueda y
   decide en cada nodo si continua por la rama izquierda o derecha.

Las dos estrategias devuelven una lista para mantener el mismo resultado
incluso si dos videojuegos tienen el mismo titulo normalizado.

## Complejidad

| Estrategia | Mejor caso | Caso promedio | Peor caso |
| --- | --- | --- | --- |
| Secuencial | Omega(1), O(1) | Theta(n) | O(n), Theta(n) |
| Arbol binario balanceado | Omega(1), O(1) | Theta(log n) | O(log n), Theta(log n) |

La complejidad del arbol depende de su altura `h`: buscar cuesta O(h). Si los
titulos se insertan ordenados, un arbol binario comun puede quedar inclinado y
su peor caso pasa a ser O(n). Para el experimento se mezclo el orden de carga
con una semilla fija, logrando una altura esperada cercana a log n. Un AVL,
que sera tratado en una etapa posterior, garantiza el balance.

## Metodo del experimento

- Se generaron colecciones de 1.000, 10.000 y 100.000 videojuegos.
- Se busco el titulo ubicado al final de la lista, que representa el peor caso
  para el recorrido secuencial.
- La construccion del arbol se hizo antes de medir: se comparo el costo de
  buscar, no el de cargar el indice.
- Cada valor es la mediana de 5 muestras; cada muestra realiza 100 busquedas.
- Se utilizo `time.perf_counter_ns`, un reloj de alta precision de Python.

## Resultados

Ejecucion realizada con `python experimento_tp2.py` en este equipo:

| N elementos | Busqueda secuencial | Busqueda en arbol |
| ---: | ---: | ---: |
| 1.000 | 0.1936 ms | 0.0012 ms |
| 10.000 | 1.8032 ms | 0.0013 ms |
| 100.000 | 19.3520 ms | 0.0012 ms |

Los tiempos absolutos pueden cambiar segun el equipo, pero la tendencia se
mantiene: al multiplicar por 100 la cantidad de datos, el tiempo secuencial
crece aproximadamente en la misma proporcion. En cambio, el arbol requiere
muchas menos comparaciones porque descarta aproximadamente la mitad de los
titulos en cada nivel cuando se mantiene balanceado.

## Conclusion tecnica

Para colecciones chicas, la busqueda secuencial es simple y suficiente. Cuando
el catalogo crece y se realizan busquedas frecuentes por titulo exacto,
conviene usar el indice en arbol por su menor tiempo de consulta esperado. La
limitacion del arbol binario comun es que no garantiza el balance; por eso una
estructura balanceada como AVL sera preferible cuando se necesite asegurar el
rendimiento en todos los casos.
