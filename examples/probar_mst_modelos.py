
import math
import random
from math import isclose

from src.grafos.generadores import (
    grafoMalla,
    grafoErdosRenyi,
    grafoGilbert,
    grafoGeografico,
    grafoBarabasiAlbert,
    grafoDorogovtsevMendes,
)


random.seed(42)


def generar_grafo(modelo, n):
    if modelo == "malla":
        if n == 30:
            return grafoMalla(5, 6)
        return grafoMalla(20, 25)

    if modelo == "erdos_renyi":
        return grafoErdosRenyi(n, 4 * n)

    if modelo == "gilbert":
        p = min(0.30, 8 / (n - 1))
        return grafoGilbert(n, p)

    if modelo == "geografico":
        r = math.sqrt(12 / (math.pi * (n - 1)))
        return grafoGeografico(n, r)

    if modelo == "barabasi_albert":
        return grafoBarabasiAlbert(n, 3)

    if modelo == "dorogovtsev_mendes":
        return grafoDorogovtsevMendes(n)

    raise ValueError("Modelo desconocido")


def es_conexo(grafo):
    if not grafo.nodos:
        return False

    adyacencias = {
        nodo: []
        for nodo in grafo.nodos
    }

    for arista in grafo.aristas:
        u = arista.origen.id
        v = arista.destino.id

        adyacencias[u].append(v)
        adyacencias[v].append(u)

    inicio = next(iter(grafo.nodos))
    visitados = {inicio}
    pila = [inicio]

    while pila:
        actual = pila.pop()

        for vecino in adyacencias[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                pila.append(vecino)

    return len(visitados) == len(grafo.nodos)


def asignar_pesos(grafo):
    for arista in grafo.aristas:
        arista.peso = round(
            random.uniform(1, 100), 2
        )


def peso_total(grafo):
    return sum(
        arista.peso
        for arista in grafo.aristas
    )


modelos = [
    "malla",
    "erdos_renyi",
    "gilbert",
    "geografico",
    "barabasi_albert",
    "dorogovtsev_mendes",
]

tamanos = [30, 500]


for modelo in modelos:
    for n in tamanos:

        # Intentar generar un grafo conexo
        for intento in range(1, 21):
            grafo = generar_grafo(modelo, n)

            if es_conexo(grafo):
                break
        else:
            raise ValueError(
                f"No se obtuvo un grafo conexo: "
                f"{modelo}_{n}"
            )

        asignar_pesos(grafo)

        # Calcular los tres MST
        mst_d = grafo.KruskalD()
        mst_i = grafo.KruskalI()
        mst_p = grafo.Prim()

        peso_d = peso_total(mst_d)
        peso_i = peso_total(mst_i)
        peso_p = peso_total(mst_p)

        # Comprobar estructura y conectividad
        for mst in (mst_d, mst_i, mst_p):
            assert len(mst.nodos) == n
            assert len(mst.aristas) == n - 1
            assert es_conexo(mst)

        # Comprobar igualdad de pesos
        assert isclose(peso_d, peso_i, abs_tol=1e-6)
        assert isclose(peso_d, peso_p, abs_tol=1e-6)

        print(
            f"{modelo}_{n}: "
            f"KruskalD={peso_d:.2f} | "
            f"KruskalI={peso_i:.2f} | "
            f"Prim={peso_p:.2f} | OK"
        )


print("\nTodas las pruebas se completaron correctamente.")
