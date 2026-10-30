import math
import random
from pathlib import Path

from src.grafos.generadores import (
    grafoErdosRenyi,
    grafoGilbert,
    grafoGeografico,
    grafoBarabasiAlbert,
    grafoDorogovtsevMendes,
)


# ============================================================
# Configuración
# ============================================================

random.seed(42)

BASE = Path("output/proyecto3")

GENERADOS = BASE / "gv" / "generados"
DIJKSTRA = BASE / "gv" / "dijkstra"

GENERADOS.mkdir(parents=True, exist_ok=True)
DIJKSTRA.mkdir(parents=True, exist_ok=True)


# ============================================================
# Funciones auxiliares
# ============================================================

def asignar_pesos(grafo):
    for arista in grafo.aristas:
        arista.peso = round(
            random.uniform(1.0, 100.0),
            2
        )


def procesar(nombre, grafo, fuente=0):
    asignar_pesos(grafo)

    # Grafo original ponderado
    grafo.guardar_gv(
        str(GENERADOS / f"{nombre}.gv"),
        mostrar_pesos=True
    )

    # Árbol de caminos más cortos
    arbol = grafo.Dijkstra(fuente)

    arbol.guardar_gv(
        str(DIJKSTRA / f"{nombre}_dijkstra.gv"),
        mostrar_pesos=True
    )

    print(
        f"{nombre}: "
        f"original={len(grafo.nodos)} nodos, "
        f"{len(grafo.aristas)} aristas | "
        f"Dijkstra={len(arbol.nodos)} nodos, "
        f"{len(arbol.aristas)} aristas"
    )


# ============================================================
# Tamaños
# ============================================================

tamanos = [30, 500]


# ============================================================
# Erdős-Rényi
# ============================================================

for n in tamanos:
    grafo = grafoErdosRenyi(
        n,
        4 * n
    )

    procesar(
        f"erdos_renyi_{n}",
        grafo
    )


# ============================================================
# Gilbert
# ============================================================

for n in tamanos:
    p = min(
        0.30,
        8 / (n - 1)
    )

    grafo = grafoGilbert(
        n,
        p
    )

    procesar(
        f"gilbert_{n}",
        grafo
    )


# ============================================================
# Geográfico
# ============================================================

for n in tamanos:
    r = math.sqrt(
        12 / (math.pi * (n - 1))
    )

    grafo = grafoGeografico(
        n,
        r
    )

    procesar(
        f"geografico_{n}",
        grafo
    )


# ============================================================
# Barabási-Albert
# ============================================================

for n in tamanos:
    grafo = grafoBarabasiAlbert(
        n,
        3
    )

    procesar(
        f"barabasi_albert_{n}",
        grafo
    )


# ============================================================
# Dorogovtsev-Mendes
# ============================================================

for n in tamanos:
    grafo = grafoDorogovtsevMendes(n)

    procesar(
        f"dorogovtsev_mendes_{n}",
        grafo
    )


print(
    "\nGeneración del Proyecto 3 terminada correctamente."
)