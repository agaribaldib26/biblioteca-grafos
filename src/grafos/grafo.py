from .nodo import Nodo
from .arista import Arista


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