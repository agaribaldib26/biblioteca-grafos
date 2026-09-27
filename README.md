# Biblioteca de Grafos

Biblioteca orientada a objetos desarrollada en Python 3 para representar, generar y exportar grafos.

## Clases principales

La biblioteca contiene las siguientes clases:

- `Nodo`: representa un vértice del grafo.
- `Arista`: representa una conexión entre dos nodos.
- `Grafo`: administra los nodos, las aristas y permite exportar el grafo en formato GraphViz.

## Modelos de generación implementados

Se implementaron los siguientes modelos:

- Malla
- Erdős-Rényi
- Gilbert
- Geográfico simple
- Barabási-Albert
- Dorogovtsev-Mendes

Las funciones correspondientes se encuentran en:

`src/grafos/generadores.py`

## Estructura del proyecto

```text
biblioteca-grafos/
│
├── src/
│   └── grafos/
│       ├── nodo.py
│       ├── arista.py
│       ├── grafo.py
│       └── generadores.py
│
├── examples/
│   ├── generar_entrega.py
│   └── pruebas de los modelos
│
├── output/
│   ├── gv/
│   └── imagenes/
│
├── README.md
└── .gitignore