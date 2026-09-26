from src.grafos.generadores import grafoGilbert


grafo = grafoGilbert(10, 0.3)

print(grafo)

grafo.guardar_gv("output/gv/gilbert_prueba.gv")