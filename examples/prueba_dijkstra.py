from src.grafos.grafo import Grafo


grafo = Grafo()

for nodo in ["A", "B", "C", "D"]:
    grafo.agregar_nodo(nodo)

grafo.agregar_arista("A", "B", 4)
grafo.agregar_arista("A", "C", 1)
grafo.agregar_arista("C", "B", 2)
grafo.agregar_arista("B", "D", 1)
grafo.agregar_arista("C", "D", 5)

arbol = grafo.Dijkstra("A")

print("Original:")
print(grafo)

print("\nÁrbol de caminos más cortos:")
print(arbol)

print("\nNodos:")
for nodo in arbol.nodos.values():
    print(nodo)

print("\nAristas:")
for arista in arbol.aristas:
    print(arista)

arbol.guardar_gv(
    "output/prueba_dijkstra.gv"
)