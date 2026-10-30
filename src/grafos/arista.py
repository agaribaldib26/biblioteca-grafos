class Arista:
    def __init__(self, origen, destino, peso=1.0):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def __repr__(self):
        return (
            f"Arista({self.origen.id}, "
            f"{self.destino.id}, "
            f"peso={self.peso})"
        )