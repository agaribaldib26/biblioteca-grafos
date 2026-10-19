from .nodo import Nodo
from .arista import Arista
from collections import deque


class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.nodos = {}
        self.aristas = []

    def agregar_nodo(self, id, x=None, y=None):
        if id not in self.nodos:
            self.nodos[id] = Nodo(id, x, y)

        return self.nodos[id]

    def agregar_arista(self, origen, destino):
        nodo_origen = self.nodos[origen]
        nodo_destino = self.nodos[destino]

        for arista in self.aristas:
            if arista.origen.id == origen and arista.destino.id == destino:
                return

            if not self.dirigido:
                if arista.origen.id == destino and arista.destino.id == origen:
                    return

        self.aristas.append(Arista(nodo_origen, nodo_destino))

    def _adyacencias(self):
        adyacencias = {nodo_id: [] for nodo_id in self.nodos}

        for arista in self.aristas:
            origen = arista.origen.id
            destino = arista.destino.id

            adyacencias[origen].append(destino)

            if not self.dirigido:
                adyacencias[destino].append(origen)

        return adyacencias

    def guardar_gv(self, nombre_archivo):
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
                archivo.write(
                    f'    "{arista.origen.id}" {operador} "{arista.destino.id}";\n'
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