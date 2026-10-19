import math
import random
from pathlib import Path

from src.grafos.generadores import (
    grafoMalla,
    grafoErdosRenyi,
    grafoGilbert,
    grafoGeografico,
    grafoBarabasiAlbert,
    grafoDorogovtsevMendes,
)


# ------------------------------------------------------------
# Configuración
# ------------------------------------------------------------

random.seed(42)

BASE = Path("output/proyecto2/gv")

CARPETAS = {
    "generados": BASE / "generados",
    "bfs": BASE / "bfs",
    "dfs_r": BASE / "dfs_r",
    "dfs_i": BASE / "dfs_i",
}

for carpeta in CARPETAS.values():
    carpeta.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Funciones auxiliares
# ------------------------------------------------------------

def validar_arbol(arbol, nombre):
    nodos = len(arbol.nodos)
    aristas = len(arbol.aristas)

    if nodos > 0 and aristas != nodos - 1:
        raise ValueError(
            f"{nombre} no cumple la propiedad de árbol: "
            f"{nodos} nodos y {aristas} aristas"
        )


def procesar_grafo(nombre, grafo, fuente):
    # Grafo original
    grafo.guardar_gv(
        str(CARPETAS["generados"] / f"{nombre}.gv")
    )

    # Recorridos
    bfs = grafo.BFS(fuente)
    dfs_r = grafo.DFS_R(fuente)
    dfs_i = grafo.DFS_I(fuente)

    # Validaciones
    validar_arbol(bfs, f"{nombre} BFS")
    validar_arbol(dfs_r, f"{nombre} DFS_R")
    validar_arbol(dfs_i, f"{nombre} DFS_I")

    # Guardar árboles
    bfs.guardar_gv(
        str(CARPETAS["bfs"] / f"{nombre}_bfs.gv")
    )

    dfs_r.guardar_gv(
        str(CARPETAS["dfs_r"] / f"{nombre}_dfs_r.gv")
    )

    dfs_i.guardar_gv(
        str(CARPETAS["dfs_i"] / f"{nombre}_dfs_i.gv")
    )

    total = len(grafo.nodos)

    print(
        f"{nombre}: "
        f"original={total} nodos, {len(grafo.aristas)} aristas | "
        f"BFS={len(bfs.nodos)}/{total} | "
        f"DFS_R={len(dfs_r.nodos)}/{total} | "
        f"DFS_I={len(dfs_i.nodos)}/{total}"
    )


# ============================================================
# 1. Malla
# ============================================================

dimensiones_malla = {
    30: (6, 5),
    100: (10, 10),
    500: (25, 20),
}

for cantidad, (m, n) in dimensiones_malla.items():
    grafo = grafoMalla(m, n)

    procesar_grafo(
        f"malla_{cantidad}",
        grafo,
        "0,0"
    )


# ============================================================
# 2. Erdős-Rényi
# ============================================================

for n in [30, 100, 500]:
    # Grado medio aproximado de 8
    m = 4 * n

    grafo = grafoErdosRenyi(n, m)

    procesar_grafo(
        f"erdos_renyi_{n}",
        grafo,
        0
    )


# ============================================================
# 3. Gilbert
# ============================================================

for n in [30, 100, 500]:
    # Mantiene aproximadamente grado medio 8
    p = min(0.30, 8 / (n - 1))

    grafo = grafoGilbert(n, p)

    procesar_grafo(
        f"gilbert_{n}",
        grafo,
        0
    )


# ============================================================
# 4. Geográfico simple
# ============================================================

for n in [30, 100, 500]:
    # Radio adaptado al número de nodos
    r = math.sqrt(12 / (math.pi * (n - 1)))

    grafo = grafoGeografico(n, r)

    procesar_grafo(
        f"geografico_{n}",
        grafo,
        0
    )


# ============================================================
# 5. Barabási-Albert
# ============================================================

for n in [30, 100, 500]:
    grafo = grafoBarabasiAlbert(n, 3)

    procesar_grafo(
        f"barabasi_albert_{n}",
        grafo,
        0
    )


# ============================================================
# 6. Dorogovtsev-Mendes
# ============================================================

for n in [30, 100, 500]:
    grafo = grafoDorogovtsevMendes(n)

    procesar_grafo(
        f"dorogovtsev_mendes_{n}",
        grafo,
        0
    )


print("\nGeneración del Proyecto 2 terminada correctamente.")