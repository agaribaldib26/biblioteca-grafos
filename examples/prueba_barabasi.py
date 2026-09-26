from src.grafos.generadores import grafoBarabasiAlbert


grafo = grafoBarabasiAlbert(10, 3)

print(grafo)

print("Grados:")
for nodo in grafo.nodos.values():
    print(f"Nodo {nodo.id}: grado {grafo.grado(nodo.id)}")

grafo.guardar_gv("output/gv/barabasi_prueba.gv")