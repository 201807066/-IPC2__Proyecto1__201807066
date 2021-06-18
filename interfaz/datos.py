import tkinter as tk
from tkinter import *
from tkinter import font

class VentanaDatos:
    def __init__(self):
        pass

    def ventanaDatos():
        ventanaDatos = Toplevel()
        ventanaDatos.title("Datos Jugadores")

        ventanaDatos.geometry('550x400')
        ventanaDatos.configure(background = "SpringGreen3")

        lb_titulo = tk.Label(ventanaDatos, text = "Block", bg = "SpringGreen3", fg = "Black", font=("Arial", 20)).place(x=230, y=20)

        lb_jugador1 = tk.Label(ventanaDatos, text = "Jugador 1", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=90, y=80)
        entrada_judador1 = StringVar()
        txt_judador1 = Entry(ventanaDatos, textvariable=entrada_judador1).place(x=90, y=110)

        lb_jugador2 = tk.Label(ventanaDatos, text = "Jugador 2", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=350, y=80)
        entrada_judador2 = StringVar()
        txt_judador2 = Entry(ventanaDatos, textvariable=entrada_judador2).place(x=350, y=110)

        lb_tamañoFila = tk.Label(ventanaDatos, text = "Tamaño Fila", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=150, y=150)
        entrada_fila = StringVar()
        txt_tamañoFila = Entry(ventanaDatos, textvariable=entrada_fila).place(x=150, y=180)

        lb_tamañoColumna = tk.Label(ventanaDatos, text = "Tamaño Columna", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=290, y=150)
        entrada_columna = StringVar()
        txt_tamañoColumna = Entry(ventanaDatos, textvariable=entrada_columna).place(x=290, y=180)

        lb_partida = tk.Label(ventanaDatos, text = "Nombre Partida", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=220, y=220)
        entrada_partida = StringVar()
        txt_partida = Entry(ventanaDatos, textvariable=entrada_partida).place(x=220, y=250)

        bt_aceptar = Button(ventanaDatos, text="Aceptar", bg ="dark green", font=("Arial", 12) ).place(x=190, y=280)
        bt_cancelar = Button(ventanaDatos, text="Cancelar", bg ="dark green", font=("Arial", 12) ).place(x=290, y=280)
