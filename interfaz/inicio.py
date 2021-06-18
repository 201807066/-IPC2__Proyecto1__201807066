import tkinter as tk
from tkinter import *
from random import *


def matrizBotones():
    root = tk.Toplevel()
    root.title("Block")
    root.geometry("900x700")
    root.config(bg = "SpringGreen3")

    fil = 8
    col = 9

    filas = Label(root, text ="Fila: " + str(fil), bg = "SpringGreen3")
    #posicion
    filas.grid(row=0, column=0)

    columnas = Label(root, text="Columnna: " + str(col), bg = "SpringGreen3")
    columnas.grid(row=1, column=0)

    nfil = 1 / fil
    ncol = 1 / col

    f1 = Frame(root)
    f1.config(bg = "#F12222")
    f1.place(relx=0.1, rely = 0.1, relwidth= 0.8, relheight = 0.8)
    #Se empieza a crear la matriz de botones
    btnlista = []

    for i in range(fil):
        btnlista.append([])
        for j in range(col):
            btnlista[i].append(Button(f1))
            btnlista[i][j].config(bg = "cyan", borderwidth=1, activebackground="Blue", relief="solid")

            btnlista[i][j].place(relx=ncol*j, rely =nfil*i, relwidth=ncol, relheight=nfil)

    root.mainloop()


def vDatos():
    #ventana.withdraw()
    global txt_tamañoFila, txt_columna

    ventanaDatos = tk.Toplevel()
    ventanaDatos.title("Datos Jugadores")

    ventanaDatos.geometry('550x400')
    ventanaDatos.configure(background = "SpringGreen3")

    lb_titulo = Label(ventanaDatos, text = "Block", bg = "SpringGreen3", fg = "Black", font=("Arial", 20)).place(x=230, y=20)

    lb_jugador1 = Label(ventanaDatos, text = "Jugador 1", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=90, y=80)
    entrada_judador1 = StringVar()
    txt_judador1 = Entry(ventanaDatos, textvariable=entrada_judador1).place(x=90, y=110)

    lb_jugador2 = Label(ventanaDatos, text = "Jugador 2", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=350, y=80)
    entrada_judador2 = StringVar()
    txt_judador2 = Entry(ventanaDatos, textvariable=entrada_judador2).place(x=350, y=110)

    lb_tamañoFila = Label(ventanaDatos, text = "Tamaño Fila", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=150, y=150)
    entrada_fila = IntVar()
    txt_tamañoFila = Entry(ventanaDatos, textvariable=entrada_fila).place(x=150, y=180)

    lb_tamañoColumna = Label(ventanaDatos, text = "Tamaño Columna", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=290, y=150)
    entrada_columna = IntVar()
    txt_tamañoColumna = Entry(ventanaDatos, textvariable=entrada_columna).place(x=290, y=180)

    lb_partida = Label(ventanaDatos, text = "Nombre Partida", bg = "SpringGreen3", fg = "Black", font=("Arial", 12)).place(x=220, y=220)
    entrada_partida = StringVar()
    txt_partida = Entry(ventanaDatos, textvariable=entrada_partida).place(x=220, y=250)

    bt_aceptar = Button(ventanaDatos, text="Aceptar", bg ="dark green", font=("Arial", 12), command = matrizBotones).place(x=190, y=280)
    bt_cancelar = Button(ventanaDatos, text="Cancelar", bg ="dark green", font=("Arial", 12), command = ventanaDatos.destroy).place(x=290, y=280)

def cerrarVentana():
    ventana.destroy()

def ayuda():
    ventanaDatos = tk.Toplevel()
    ventanaDatos.title("Datos Jugadores")

    ventanaDatos.geometry('550x400')
    ventanaDatos.configure(background = "SpringGreen3")

    lb_titulo = Label(ventanaDatos, text = "Block", bg = "SpringGreen3", fg = "Black", font=("Arial", 20)).place(x=230, y=20)


ventana = tk.Tk()
ventana.title("Inicio")
#tamaño ancho x alto
ventana.geometry('380x300')
ventana.configure(background = "SpringGreen3")

titulo = Label(ventana, text="Block", bg = "SpringGreen3", fg = "black", font=("Arial", 20)).place(x=150, y=20)
bt_inicio = Button(ventana, text="Iniciar Juego", bg ="dark green", font=("Arial", 12), command=vDatos).place(x=60, y=90)
bt_cargar = Button(ventana, text="Cargar Partida", bg ="dark green", font=("Arial", 12) ).place(x=210, y=90)
bt_reporte = Button(ventana, text="Reporte HTML", bg ="dark green", font=("Arial", 12) ).place(x=60, y=160)
bt_ayuda = Button(ventana, text="Ayuda", bg ="dark green", font=("Arial", 12), command = ayuda).place(x=210, y=160)

ventana.mainloop()
