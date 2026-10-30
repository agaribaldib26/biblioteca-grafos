# Biblioteca de Grafos

Biblioteca orientada a objetos desarrollada en **Python 3** para representar grafos dirigidos y no dirigidos, generar grafos mediante distintos modelos, realizar recorridos y calcular árboles de caminos más cortos. Incluye exportación al formato **GraphViz (`.gv`)** y visualizaciones de los resultados.

Proyecto desarrollado como parte de la asignatura **Diseño y Análisis de Algoritmos**.

## Funcionalidades

### Clases principales

- **`Nodo`** (`src/grafos/nodo.py`): representa un vértice, con identificador y coordenadas opcionales `x`, `y`.
- **`Arista`** (`src/grafos/arista.py`): representa una conexión entre dos nodos y admite un peso; de forma predeterminada, `peso=1.0`.
- **`Grafo`** (`src/grafos/grafo.py`): administra nodos y aristas, admite grafos dirigidos o no dirigidos y permite ejecutar algoritmos y exportar archivos `.gv`.

### Modelos de generación — Proyecto 1

Los generadores se implementan en `src/grafos/generadores.py`:

| Modelo | Función | Descripción |
|---|---|---|
| Malla | `grafoMalla(m, n, dirigido=False)` | Conecta los nodos de una cuadrícula de `m` columnas y `n` filas. |
| Erdős–Rényi | `grafoErdosRenyi(n, m, dirigido=False)` | Selecciona `m` aristas distintas entre `n` nodos. |
| Gilbert | `grafoGilbert(n, p, dirigido=False)` | Crea cada arista posible con probabilidad `p`. |
| Geográfico simple | `grafoGeografico(n, r, dirigido=False)` | Une nodos cuya distancia euclidiana es menor o igual que `r`. |
| Barabási–Albert | `grafoBarabasiAlbert(n, d, dirigido=False)` | Agrega nodos con conexión preferencial según el grado. |
| Dorogovtsev–Mendes | `grafoDorogovtsevMendes(n, dirigido=False)` | Parte de un triángulo y agrega nodos conectados a los extremos de una arista elegida al azar. |

**Entregables del Proyecto 1:** 18 grafos `.gv` (50, 200 y 500 nodos por modelo) y 18 imágenes PNG.

### Recorridos — Proyecto 2

La clase `Grafo` implementa los métodos:

- **`BFS(s)`**: recorrido en anchura; devuelve el árbol de búsqueda desde la fuente `s`.
- **`DFS_R(s)`**: recorrido en profundidad recursivo; devuelve el árbol correspondiente.
- **`DFS_I(s)`**: recorrido en profundidad iterativo mediante una pila; devuelve el árbol correspondiente.

Los árboles contienen los nodos alcanzables desde `s`, por lo que pueden incluir menos nodos que el grafo original si este es desconectado.

**Entregables del Proyecto 2:** 18 grafos originales (30, 100 y 500 nodos por modelo), 54 árboles calculados y 72 imágenes PNG.

### Caminos mínimos — Proyecto 3

- **`Dijkstra(s)`**: calcula un árbol de caminos más cortos desde `s` en un grafo con **pesos no negativos**.
- Las aristas de la biblioteca tienen un atributo `peso`; los ejemplos de la entrega asignan pesos aleatorios entre **1 y 100**, redondeados a dos decimales.
- En el grafo calculado, cada nodo muestra la distancia mínima desde la fuente en su identificador, por ejemplo: `nodo_2 (22.45)`.
- El método `guardar_gv(nombre_archivo, mostrar_pesos=True)` permite mostrar los pesos de las aristas en el archivo GraphViz.

**Entregables del Proyecto 3:** 10 grafos originales (30 y 500 nodos para cada uno de los cinco generadores aleatorios), 10 árboles de Dijkstra y 20 imágenes PNG.

## Estructura del repositorio

```text
biblioteca-grafos/
├── src/
│   └── grafos/
│       ├── nodo.py
│       ├── arista.py
│       ├── grafo.py
│       └── generadores.py
├── examples/
│   ├── generar_entrega.py
│   ├── generar_entrega_proyecto2.py
│   ├── generar_entrega_proyecto3.py
│   ├── prueba_recorridos.py
│   ├── prueba_dijkstra.py
│   └── ... otros ejemplos de prueba
├── output/
│   ├── gv/                  # Proyecto 1
│   ├── imagenes/            # Proyecto 1
│   ├── proyecto2/
│   │   ├── gv/
│   │   └── imagenes/
│   └── proyecto3/
│       ├── gv/
│       └── imagenes/
├── README.md
└── .gitignore
```

## Requisitos y ejecución

- Python 3.
- Para visualizar o renderizar archivos `.gv`: **Graphviz** y/o **Gephi** (herramientas externas; no son necesarias para ejecutar los algoritmos de la biblioteca).
- Los generadores y algoritmos de la biblioteca usan módulos de la biblioteca estándar de Python.

Desde la **raíz del repositorio**, ejecutar en PowerShell:

```powershell
# Generación del Proyecto 1
python -m examples.generar_entrega

# Generación del Proyecto 2
python -m examples.generar_entrega_proyecto2

# Generación del Proyecto 3
python -m examples.generar_entrega_proyecto3
```

Los comandos anteriores generan los archivos `.gv` correspondientes. Las imágenes PNG incluidas en el repositorio fueron preparadas a partir de esos grafos utilizando herramientas de visualización.

### Pruebas de ejemplo

```powershell
python -m examples.prueba_recorridos
python -m examples.prueba_dijkstra
```

### Ejemplo de uso

```python
from src.grafos.generadores import grafoErdosRenyi

# Crear un grafo no dirigido y recorrerlo desde el nodo 0
grafo = grafoErdosRenyi(30, 120)
arbol_bfs = grafo.BFS(0)
arbol_bfs.guardar_gv("output/ejemplo_bfs.gv")
```

Para ejecutar Dijkstra sobre un grafo generado, primero deben asignarse **pesos no negativos** a sus aristas. En el script `examples/generar_entrega_proyecto3.py` se realiza esa asignación y se guardan tanto los grafos ponderados originales como los árboles de caminos mínimos.

## Notas de reproducibilidad

Los scripts de generación utilizan la semilla aleatoria `42`, de modo que los resultados son reproducibles al ejecutarlos con la misma implementación y configuración. Los pesos del Proyecto 3 se guardan en los archivos `.gv`, y las distancias acumuladas se muestran en las etiquetas de los nodos de los árboles calculados.

## Repositorio

[GitHub — biblioteca-grafos](https://github.com/agaribaldib26/biblioteca-grafos)
