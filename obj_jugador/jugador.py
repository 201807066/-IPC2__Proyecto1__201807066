import  os, sys

class Jugador(object):

    def __init__(self, nombre, color, punteo, turno, tiempo, ganador):
        self.nombre = nombre
        self.color = color
        self.punteo = punteo
        self.turno = turno
        self.tiempo = tiempo
        self.ganador = ganador
