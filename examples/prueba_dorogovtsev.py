from src.grafos.generadores import grafoDorogovtsevMendes


grafo = grafoDorogovtsevMendes(10)

print(grafo)

print("Grados:")
for nodo in grafo.nodos.values():
    print(f"Nodo {nodo.id}: grado {grafo.grado(nodo.id)}")

grafo.guardar_gv("output/gv/dorogovtsev_prueba.gv")