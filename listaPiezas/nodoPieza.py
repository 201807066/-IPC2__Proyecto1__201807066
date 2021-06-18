from graphviz import Digraph

#Creamos la clase Nodo
class NodoPieza():

    def __init__(self, id = None, nombre = None, siguiente = None, anterior = None):
        self.id = id
        self.nombre = nombre
        self.siguiente = siguiente
        self.anterior = anterior


class ListaPiezas():
    
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None
    
    def agregar(self, id, nombre):
        if self.vacia():
            self.primero = self.ultimo = NodoPieza(id, nombre)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = NodoPieza(id, nombre)
            self.ultimo.anterior = aux


    def mostrar(self):
        aux = self.primero
        while aux:
            print("ID: " + str(aux.id) + " Nombre: " + aux.nombre)
            aux = aux.siguiente


lista = ListaPiezas()

lista.agregar(1, "Pieza1")
lista.agregar(2, "Pieza2")
lista.agregar(3, "Pieza3")
lista.agregar(4, "Pieza4")
lista.agregar(5, "Pieza5")
lista.agregar(6, "Pieza6")
lista.mostrar()