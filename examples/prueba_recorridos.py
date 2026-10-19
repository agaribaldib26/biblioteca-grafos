from src.grafos.grafo import Grafo


grafo = Grafo()

for i in range(1, 7):
    grafo.agregar_nodo(i)

grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(2, 4)
grafo.agregar_arista(2, 5)
grafo.agregar_arista(3, 5)
grafo.agregar_arista(4, 6)
grafo.agregar_arista(5, 6)

bfs = grafo.BFS(1)
dfs_r = grafo.DFS_R(1)
dfs_i = grafo.DFS_I(1)

print("Original:")
print(grafo)

print("\nBFS:")
print(bfs)
for arista in bfs.aristas:
    print(arista)

print("\nDFS recursivo:")
print(dfs_r)
for arista in dfs_r.aristas:
    print(arista)

print("\nDFS iterativo:")
print(dfs_i)
for arista in dfs_i.aristas:
    print(arista)