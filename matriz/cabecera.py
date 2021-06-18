from matriz.nodoMatriz import *

class listaEncabezado():
    def __init__(self, head = None):
        self.head = head

        
    def agregarEncabezado(self, nuevoNodo):
        if self.head == None:
            self.head = nuevoNodo
        elif nuevoNodo.id < self.head.id:
            nuevoNodo.siguiente = self.head
            self.head.anterior = nuevoNodo
            self.head = nuevoNodo
        else:
            aux = self.head
            while aux.siguiente != None:
                if nuevoNodo.id < aux.siguiente.id:
                    nuevoNodo.siguiente = aux.siguiente
                    aux.siguiente.anterior = nuevoNodo
                    nuevoNodo.anterior = aux
                    aux.siguiente = nuevoNodo
                    break
                aux = aux.siguiente

            if aux.siguiente == None:
                aux.siguiente = nuevoNodo
                nuevoNodo.anterior = aux
    
    def getEncabezado(self, id):
        aux = self.primero
        while aux != None:
            if aux.id == id:
                return aux
            aux = aux.siguiente
        return None
        
