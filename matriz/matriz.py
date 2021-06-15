import os, sys, time
from typing import Sized
from graphviz import Digraph

from matriz.nodoMatriz import *
from matriz.cabecera import *

class Matriz:
    def __init__(self):
        self.efilas = listaEncabezado()
        self.ecolumnas = listaEncabezado()
    
    def insertar(self, posX, posY, valor):
        nuevo = Nodo(posX, posY, valor)

        #Insercion de encabezados por filas 
        efila = self.efilas.getEncabezado()
        if efila == None:
            efila = nodoCabeceras(posX)
            efila.accesoNodo = nuevo
            self.efilas.setEncabezado(efila)
        else:
            if nuevo.columna < efila.accesoNodo.columna:
                nuevo.derecha = efila.accesoNodo
                efila.accesoNodo.izquierda = nuevo
                efila.accesoNodo = nuevo
            else:
                aux = efila.accesoNodo
                while aux.derecha != None:
                    if nuevo.columna < aux.derecha.columna:
                        nuevo.derecha = aux.derecha
                        aux.derecha.izquierda = nuevo
                        nuevo.izquierda = aux
                        aux.derecha = nuevo
                        break
                    aux = aux.derecha   

                if aux.derecha == None:
                    aux.derecha = nuevo
                    nuevo.izquierda = aux

        #Insercion de encabezados por columnas 
        ecolumna = self.ecolumna.getEncabezado()
        if ecolumna == None:
            ecolumna = nodoCabeceras(posY)
            ecolumna.accesoNodo = nuevo
            self.ecolumna.setEncabezado(ecolumna)
        else:
            if nuevo.fila < ecolumna.accesoNodo.fila:
                nuevo.abajo = ecolumna.accesoNodo
                ecolumna.accesoNodo.arriba = nuevo
                ecolumna.accesoNodo = nuevo
            else:
                aux = ecolumna.accesoNodo
                while aux.abajo != None:
                    if nuevo.fila < aux.abajo.fila:
                        nuevo.abajo = aux.abajo
                        aux.abajo.arriba = nuevo
                        nuevo.arriba = aux
                        aux.abajo = nuevo
                        break
                    aux = aux.abajo   

                if aux.abajo == None:
                    aux.abajo = nuevo
                    nuevo.arriba = aux

    def recorrerFilas(self):
        efila = self.efilas.head
        print("Recorrido por filas")

        while efila != None:
            aux = efila.accesoNodo
            print("\nFila" + str(aux.fila))
            print("Columna      Valor")
            while aux != None:
                print(str(aux.columna) + "      " + aux.valor)
                aux = aux.derecha
            
            efila = efila.siguiente 
        print("Fin del recorrido por filas ")

    def recorridoColumnas(self):
        ecolumna = self.ecolumnas.head
        print("Recorrido por columnas")

        while ecolumna != None:
            aux = ecolumna.accesoNodo
            print("\nColumna ", str(aux.columna))
            print("Fila     Dato")
            while aux != None:
                print(str(aux.fila) + "      " + aux.valor)
                aux = aux.abajo
            
            ecolumna = ecolumna.abajo
        print("Fin del recorrido por columnas")

"""
Se define el diagrama
se define que tendra forma cuadrada los nodos
se crean las cabeceras para filas y columnas
se define sus caracteristicas
se dibujan sus punteros, ya sean dobles o simples
se alinean
se añaden sus elementos, recorriendo la matriz fila por fila
se dibujan las punteros de ambas cabeceras al primer elemento
se dibujan los punteros del resto de elementos en las filas
se alinean los nodos
se recorren el resto de las filas
"""

def imagen_dor(matriz):
    f = Digraph(format = "png", name = "salida")
    f.attr(size = "8.5")

    
