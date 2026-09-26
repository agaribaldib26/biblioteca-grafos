from src.grafos.generadores import grafoGeografico


grafo = grafoGeografico(10, 0.4)

print(grafo)

print("Coordenadas:")
for nodo in grafo.nodos.values():
    print(f"Nodo {nodo.id}: ({nodo.x:.3f}, {nodo.y:.3f})")

grafo.guardar_gv("output/gv/geografico_prueba.gv")