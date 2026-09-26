class Nodo:
    def __init__(self, id, x=None, y=None):
        self.id = id
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Nodo({self.id})"