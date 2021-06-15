class Nodo:

    def __init__(self, posX, posY, valor):
        self.posX = posX
        self.posY = posY
        self.valor = valor
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None


class nodoCabeceras:
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None
        