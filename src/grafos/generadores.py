from .grafo import Grafo

import random

import math

def grafoMalla(m, n, dirigido=False):
    """
    Genera grafo de malla.

    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    if m <= 1 or n <= 1:
        raise ValueError("m y n deben ser mayores que 1")

    grafo = Grafo(dirigido)

    for i in range(m):
        for j in range(n):
            nodo_id = f"{i},{j}"
            grafo.agregar_nodo(nodo_id)

    for i in range(m):
        for j in range(n):
            actual = f"{i},{j}"

            if i < m - 1:
                derecha = f"{i + 1},{j}"
                grafo.agregar_arista(actual, derecha)

            if j < n - 1:
                abajo = f"{i},{j + 1}"
                grafo.agregar_arista(actual, abajo)

    return grafo

def grafoErdosRenyi(n, m, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi.

    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    if n <= 0:
        raise ValueError("n debe ser mayor que 0")

    if m < n - 1:
        raise ValueError("m debe ser mayor o igual que n - 1")

    if dirigido:
        max_aristas = n * (n - 1)
    else:
        max_aristas = n * (n - 1) // 2

    if m > max_aristas:
        raise ValueError(
            f"m no puede ser mayor que {max_aristas} para n={n}"
        )

    grafo = Grafo(dirigido)

    for i in range(n):
        grafo.agregar_nodo(i)

    posibles_aristas = []

    if dirigido:
        for i in range(n):
            for j in range(n):
                if i != j:
                    posibles_aristas.append((i, j))
    else:
        for i in range(n):
            for j in range(i + 1, n):
                posibles_aristas.append((i, j))

    aristas_elegidas = random.sample(posibles_aristas, m)

    for origen, destino in aristas_elegidas:
        grafo.agregar_arista(origen, destino)

    return grafo

def grafoGilbert(n, p, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Gilbert.

    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    if n <= 0:
        raise ValueError("n debe ser mayor que 0")

    if p <= 0 or p >= 1:
        raise ValueError("p debe estar entre 0 y 1")

    grafo = Grafo(dirigido)

    for i in range(n):
        grafo.agregar_nodo(i)

    if dirigido:
        for i in range(n):
            for j in range(n):
                if i != j and random.random() < p:
                    grafo.agregar_arista(i, j)
    else:
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    grafo.agregar_arista(i, j)

    return grafo

def grafoGeografico(n, r, dirigido=False):
    """
    Genera grafo aleatorio con el modelo geográfico simple.

    :param n: número de nodos (> 0)
    :param r: distancia máxima para crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    if n <= 0:
        raise ValueError("n debe ser mayor que 0")

    if r <= 0 or r >= 1:
        raise ValueError("r debe estar entre 0 y 1")

    grafo = Grafo(dirigido)

    for i in range(n):
        x = random.random()
        y = random.random()
        grafo.agregar_nodo(i, x, y)

    if dirigido:
        for i in range(n):
            for j in range(n):
                if i != j:
                    nodo_i = grafo.nodos[i]
                    nodo_j = grafo.nodos[j]

                    distancia = math.sqrt(
                        (nodo_i.x - nodo_j.x) ** 2
                        + (nodo_i.y - nodo_j.y) ** 2
                    )

                    if distancia <= r:
                        grafo.agregar_arista(i, j)

    else:
        for i in range(n):
            for j in range(i + 1, n):
                nodo_i = grafo.nodos[i]
                nodo_j = grafo.nodos[j]

                distancia = math.sqrt(
                    (nodo_i.x - nodo_j.x) ** 2
                    + (nodo_i.y - nodo_j.y) ** 2
                )

                if distancia <= r:
                    grafo.agregar_arista(i, j)

    return grafo

def grafoBarabasiAlbert(n, d, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert.

    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    if n <= 0:
        raise ValueError("n debe ser mayor que 0")

    if d <= 1:
        raise ValueError("d debe ser mayor que 1")

    if d >= n:
        raise ValueError("d debe ser menor que n")

    grafo = Grafo(dirigido)

    for i in range(d):
        grafo.agregar_nodo(i)

    for i in range(d):
        for j in range(i + 1, d):
            grafo.agregar_arista(i, j)

    for nuevo in range(d, n):
        grafo.agregar_nodo(nuevo)

        candidatos = list(range(nuevo))
        elegidos = []

        while len(elegidos) < d:
            pesos = []

            for candidato in candidatos:
                pesos.append(grafo.grado(candidato))

            seleccionado = random.choices(
                candidatos,
                weights=pesos,
                k=1
            )[0]

            if seleccionado not in elegidos:
                elegidos.append(seleccionado)

        for destino in elegidos:
            grafo.agregar_arista(nuevo, destino)

    return grafo

def grafoDorogovtsevMendes(n, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Dorogovtsev-Mendes.

    :param n: número de nodos (>= 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """

    if n < 3:
        raise ValueError("n debe ser mayor o igual que 3")

    grafo = Grafo(dirigido)

    grafo.agregar_nodo(0)
    grafo.agregar_nodo(1)
    grafo.agregar_nodo(2)

    grafo.agregar_arista(0, 1)
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(2, 0)

    for nuevo in range(3, n):
        grafo.agregar_nodo(nuevo)

        arista_elegida = random.choice(grafo.aristas)

        origen = arista_elegida.origen.id
        destino = arista_elegida.destino.id

        grafo.agregar_arista(nuevo, origen)
        grafo.agregar_arista(nuevo, destino)

    return grafo