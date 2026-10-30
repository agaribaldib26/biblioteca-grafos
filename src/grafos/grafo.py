from .nodo import Nodo
from .arista import Arista
from collections import deque
import heapq
from itertools import count


class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.nodos = {}
        self.aristas = []

    def agregar_nodo(self, id, x=None, y=None):
        if id not in self.nodos:
            self.nodos[id] = Nodo(id, x, y)

        return self.nodos[id]

    def agregar_arista(self, origen, destino, peso=1.0):
        nodo_origen = self.nodos[origen]
        nodo_destino = self.nodos[destino]

        for arista in self.aristas:
            if arista.origen.id == origen and arista.destino.id == destino:
                return

            if not self.dirigido:
                if arista.origen.id == destino and arista.destino.id == origen:
                    return

        self.aristas.append(Arista(nodo_origen, nodo_destino, peso))
   
    def _adyacencias(self):
        adyacencias = {nodo_id: [] for nodo_id in self.nodos}

        for arista in self.aristas:
            origen = arista.origen.id
            destino = arista.destino.id

            adyacencias[origen].append(destino)

            if not self.dirigido:
                adyacencias[destino].append(origen)

        return adyacencias

    def guardar_gv(self, nombre_archivo, mostrar_pesos=False):
        tipo_grafo = "digraph" if self.dirigido else "graph"
        operador = "->" if self.dirigido else "--"

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"{tipo_grafo} G {{\n")

            for nodo in self.nodos.values():
                if nodo.x is not None and nodo.y is not None:
                    archivo.write(
                        f'    "{nodo.id}" [pos="{nodo.x},{nodo.y}!"];\n'
                    )
                else:
                    archivo.write(f'    "{nodo.id}";\n')

            for arista in self.aristas:
                if mostrar_pesos:
                    archivo.write(
                        f'    "{arista.origen.id}" {operador} '
                        f'"{arista.destino.id}" '
                        f'[label="{arista.peso:.2f}"];\n'
                    )
                else:
                    archivo.write(
                        f'    "{arista.origen.id}" {operador} '
                        f'"{arista.destino.id}";\n'
                    )

            archivo.write("}\n")

    def __repr__(self):
        return (
            f"Grafo(nodos={len(self.nodos)}, "
            f"aristas={len(self.aristas)}, "
            f"dirigido={self.dirigido})"
        )

    def grado(self, nodo_id):
        grado = 0

        for arista in self.aristas:
            if arista.origen.id == nodo_id:
                grado += 1

            if arista.destino.id == nodo_id:
                grado += 1

        return grado

    def BFS(self, s):
        if s not in self.nodos:
            raise ValueError(f"El nodo {s} no existe en el grafo")

        adyacencias = self._adyacencias()

        arbol = Grafo(self.dirigido)

        nodo_fuente = self.nodos[s]
        arbol.agregar_nodo(
            s,
            nodo_fuente.x,
            nodo_fuente.y
        )

        visitados = {s}
        cola = deque([s])

        while cola:
            actual = cola.popleft()

            for vecino in adyacencias[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

                    nodo_vecino = self.nodos[vecino]

                    arbol.agregar_nodo(
                        vecino,
                        nodo_vecino.x,
                        nodo_vecino.y
                    )

                    arbol.agregar_arista(actual, vecino)

        return arbol

    def DFS_R(self, s):
        if s not in self.nodos:
            raise ValueError(f"El nodo {s} no existe en el grafo")

        adyacencias = self._adyacencias()

        arbol = Grafo(self.dirigido)
        visitados = set()

        def visitar(actual):
            visitados.add(actual)

            nodo_actual = self.nodos[actual]

            if actual not in arbol.nodos:
                arbol.agregar_nodo(
                    actual,
                    nodo_actual.x,
                    nodo_actual.y
                )

            for vecino in adyacencias[actual]:
                if vecino not in visitados:
                    nodo_vecino = self.nodos[vecino]

                    arbol.agregar_nodo(
                        vecino,
                        nodo_vecino.x,
                        nodo_vecino.y
                    )

                    arbol.agregar_arista(actual, vecino)

                    visitar(vecino)

        visitar(s)

        return arbol

    def DFS_I(self, s):
        if s not in self.nodos:
            raise ValueError(f"El nodo {s} no existe en el grafo")

        adyacencias = self._adyacencias()

        arbol = Grafo(self.dirigido)
        visitados = set()

        pila = [(s, None)]

        while pila:
            actual, padre = pila.pop()

            if actual in visitados:
                continue

            visitados.add(actual)

            nodo_actual = self.nodos[actual]
            arbol.agregar_nodo(
                actual,
                nodo_actual.x,
                nodo_actual.y
            )

            if padre is not None:
                arbol.agregar_arista(padre, actual)

            for vecino in reversed(adyacencias[actual]):
                if vecino not in visitados:
                    pila.append((vecino, actual))

        return arbol

    def _adyacencias_pesadas(self):
        adyacencias = {
            nodo_id: []
            for nodo_id in self.nodos
        }

        for arista in self.aristas:
            if arista.peso < 0:
                raise ValueError(
                    "Dijkstra no admite pesos negativos"
                )

            origen = arista.origen.id
            destino = arista.destino.id
            peso = arista.peso

            adyacencias[origen].append(
                (destino, peso)
            )

            if not self.dirigido:
                adyacencias[destino].append(
                    (origen, peso)
                )

        return adyacencias

    def Dijkstra(self, s):
        if s not in self.nodos:
            raise ValueError(
                f"El nodo {s} no existe en el grafo"
            )

        adyacencias = self._adyacencias_pesadas()

        distancias = {
            nodo_id: float("inf")
            for nodo_id in self.nodos
        }

        anteriores = {
            nodo_id: None
            for nodo_id in self.nodos
        }

        distancias[s] = 0.0

        contador = count()
        cola = [(0.0, next(contador), s)]

        while cola:
            distancia_actual, _, actual = heapq.heappop(
                cola
            )

            if distancia_actual > distancias[actual]:
                continue

            for vecino, peso in adyacencias[actual]:
                nueva_distancia = (
                    distancia_actual + peso
                )

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = (
                        actual,
                        peso
                    )

                    heapq.heappush(
                        cola,
                        (
                            nueva_distancia,
                            next(contador),
                            vecino
                        )
                    )

        arbol = Grafo(self.dirigido)
        etiquetas = {}

        for nodo_id, distancia in distancias.items():
            if distancia == float("inf"):
                continue

            nodo_original = self.nodos[nodo_id]

            etiqueta = f"{nodo_id} ({distancia:.2f})"
            etiquetas[nodo_id] = etiqueta

            arbol.agregar_nodo(
                etiqueta,
                nodo_original.x,
                nodo_original.y
            )

        for nodo_id, anterior in anteriores.items():
            if anterior is None:
                continue

            padre, peso = anterior

            arbol.agregar_arista(
                etiquetas[padre],
                etiquetas[nodo_id],
                peso
            )

        return arbol