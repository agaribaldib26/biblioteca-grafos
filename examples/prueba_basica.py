from src.grafos.grafo import Grafo


grafo = Grafo()

grafo.agregar_nodo(1)
grafo.agregar_nodo(2)
grafo.agregar_nodo(3)

grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 1)

print(grafo)

print("Nodos:")
for nodo in grafo.nodos.values():
    print(nodo)

print("Aristas:")
for arista in grafo.aristas:
    print(arista)
grafo.guardar_gv("output/gv/prueba_basica.gv")