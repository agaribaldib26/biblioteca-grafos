from src.grafos.generadores import grafoMalla


grafo = grafoMalla(3, 2)

print(grafo)

grafo.guardar_gv("output/gv/malla_prueba.gv")