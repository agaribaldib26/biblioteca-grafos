class Arista:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def __repr__(self):
        return f"Arista({self.origen.id}, {self.destino.id})"