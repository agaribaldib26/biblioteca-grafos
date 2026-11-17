
from src.grafos.grafo import Grafo


grafo = Grafo()

for nodo in ["A", "B", "C", "D"]:
    grafo.agregar_nodo(nodo)

grafo.agregar_arista("A", "B", 4)
grafo.agregar_arista("A", "C", 1)
grafo.agregar_arista("B", "C", 2)
grafo.agregar_arista("B", "D", 1)
grafo.agregar_arista("C", "D", 5)

mst = grafo.KruskalD()

print("Grafo original:")
print(grafo)

print("\nÁrbol de expansión mínima:")
print(mst)

print("\nAristas del MST:")
for arista in mst.aristas:
    print(arista)

peso_total = sum(
    arista.peso for arista in mst.aristas
)

print(f"\nPeso total del MST: {peso_total:.2f}")

mst.guardar_gv(
    "output/prueba_mst.gv",
    mostrar_pesos=True
)


# ============================================================
# Kruskal inverso
# ============================================================

mst_inverso = grafo.KruskalI()

print("\nKruskal inverso:")
print(mst_inverso)

print("\nAristas:")
for arista in mst_inverso.aristas:
    print(arista)

peso_inverso = sum(
    arista.peso for arista in mst_inverso.aristas
)

print(
    f"\nPeso total Kruskal inverso: "
    f"{peso_inverso:.2f}"
)

mst_inverso.guardar_gv(
    "output/prueba_mst_inverso.gv",
    mostrar_pesos=True
)

# ============================================================
# Prim
# ============================================================

mst_prim = grafo.Prim()

print("\nPrim:")
print(mst_prim)

print("\nAristas:")
for arista in mst_prim.aristas:
    print(arista)

peso_prim = sum(
    arista.peso for arista in mst_prim.aristas
)

print(
    f"\nPeso total Prim: {peso_prim:.2f}"
)

mst_prim.guardar_gv(
    "output/prueba_mst_prim.gv",
    mostrar_pesos=True
)

# ============================================================
# Comparación de algoritmos
# ============================================================

from math import isclose

print("\nComparación de pesos del MST:")
print(f"Kruskal directo: {peso_total:.2f}")
print(f"Kruskal inverso: {peso_inverso:.2f}")
print(f"Prim:            {peso_prim:.2f}")

assert isclose(peso_total, peso_inverso)
assert isclose(peso_total, peso_prim)

print("\nLos tres algoritmos coinciden en el peso del MST.")

