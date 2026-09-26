from src.grafos.generadores import grafoErdosRenyi


grafo = grafoErdosRenyi(10, 15)

print(grafo)

grafo.guardar_gv("output/gv/erdos_renyi_prueba.gv")