import random

from src.grafos.generadores import (
    grafoMalla,
    grafoErdosRenyi,
    grafoGilbert,
    grafoGeografico,
    grafoBarabasiAlbert,
    grafoDorogovtsevMendes,
)


random.seed(42)


# ============================================================
# Malla
# ============================================================

dimensiones_malla = {
    50: (10, 5),
    200: (20, 10),
    500: (25, 20),
}

for n_nodos, (m, n) in dimensiones_malla.items():
    grafo = grafoMalla(m, n)
    nombre = f"output/gv/malla_{n_nodos}.gv"
    grafo.guardar_gv(nombre)

    print(
        f"Malla {n_nodos}: "
        f"{len(grafo.nodos)} nodos, "
        f"{len(grafo.aristas)} aristas"
    )


# ============================================================
# Erdős-Rényi
# ============================================================

for n in [50, 200, 500]:
    m = 2 * n

    grafo = grafoErdosRenyi(n, m)
    nombre = f"output/gv/erdos_renyi_{n}.gv"
    grafo.guardar_gv(nombre)

    print(
        f"Erdos-Renyi {n}: "
        f"{len(grafo.nodos)} nodos, "
        f"{len(grafo.aristas)} aristas"
    )


# ============================================================
# Gilbert
# ============================================================

for n in [50, 200, 500]:
    grafo = grafoGilbert(n, 0.05)
    nombre = f"output/gv/gilbert_{n}.gv"
    grafo.guardar_gv(nombre)

    print(
        f"Gilbert {n}: "
        f"{len(grafo.nodos)} nodos, "
        f"{len(grafo.aristas)} aristas"
    )


# ============================================================
# Geográfico simple
# ============================================================

for n in [50, 200, 500]:
    grafo = grafoGeografico(n, 0.1)
    nombre = f"output/gv/geografico_{n}.gv"
    grafo.guardar_gv(nombre)

    print(
        f"Geografico {n}: "
        f"{len(grafo.nodos)} nodos, "
        f"{len(grafo.aristas)} aristas"
    )


# ============================================================
# Barabási-Albert
# ============================================================

for n in [50, 200, 500]:
    grafo = grafoBarabasiAlbert(n, 3)
    nombre = f"output/gv/barabasi_albert_{n}.gv"
    grafo.guardar_gv(nombre)

    print(
        f"Barabasi-Albert {n}: "
        f"{len(grafo.nodos)} nodos, "
        f"{len(grafo.aristas)} aristas"
    )


# ============================================================
# Dorogovtsev-Mendes
# ============================================================

for n in [50, 200, 500]:
    grafo = grafoDorogovtsevMendes(n)
    nombre = f"output/gv/dorogovtsev_mendes_{n}.gv"
    grafo.guardar_gv(nombre)

    print(
        f"Dorogovtsev-Mendes {n}: "
        f"{len(grafo.nodos)} nodos, "
        f"{len(grafo.aristas)} aristas"
    )


print("\nGeneración terminada.")