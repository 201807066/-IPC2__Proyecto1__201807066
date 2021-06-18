from random import randint
import tkinter as tk
from tkinter import *

def cambiar(frame):
    frame.tkraise()
    
window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#Frame 1 -> Inicio
#Frame 2 -> Datos
#Frame 3 -> Matriz
#Frame 4 -> Ayuda
inicio = tk.Frame(window)
datos = tk.Frame(window)
matriz = tk.Frame(window)
ayuda = tk.Frame(window)

for frame in (inicio, datos, matriz):
    frame.grid(row=0,column=0,sticky='nsew')


#==================Frame 1 code
frame1_title=  tk.Label(inicio, text='', font='times 35', bg='SpringGreen3')
frame1_title.pack(fill='both', expand=True)


titulo = Label(inicio, text="Block", bg = "SpringGreen3", fg = "black", font=("Arial", 70)).place(x=650, y=20)
bt_inicio = Button(inicio, text="Iniciar Juego", bg ="dark green", font=("Arial", 40), command=lambda:cambiar(datos)).place(x=300, y=250)
bt_cargar = Button(inicio, text="Cargar Partida", bg ="dark green", font=("Arial", 40) ).place(x=800, y=250)
bt_reporte = Button(inicio, text="Reporte HTML", bg ="dark green", font=("Arial", 40) ).place(x=300, y=500)
bt_ayuda = Button(inicio, text="Ayuda", bg ="dark green", font=("Arial", 40), command = "ayuda").place(x=900, y=500)


#==================Frame 2 code

frame2_title=  tk.Label(datos, text='', font='times 35', bg='SpringGreen3')
frame2_title.pack(fill='both', expand=True)

entrada_judador1 = StringVar()
entrada_judador2 = StringVar()
entrada_fila = IntVar()
entrada_columna = IntVar()
entrada_partida = StringVar()

lb_titulo = Label(datos, text = "Block", bg = "SpringGreen3", fg = "Black", font=("Arial", 70)).place(x=650, y=20)
lb_jugador1 = Label(datos, text = "Jugador 1", bg = "SpringGreen3", fg = "Black", font=("Arial", 25)).place(x=450, y=110)
txt_judador1 = Entry(datos, textvariable=entrada_judador1, font=("Arial", 20)).place(x=450, y=160)

lb_jugador2 = Label(datos, text = "Jugador 2", bg = "SpringGreen3", fg = "Black", font=("Arial", 25)).place(x=800, y=110)

txt_judador2 = Entry(datos, textvariable=entrada_judador2, font=("Arial", 20)).place(x=800, y=160)

lb_tamañoFila = Label(datos, text = "Tamaño Fila", bg = "SpringGreen3", fg = "Black", font=("Arial", 25)).place(x=450, y=200)
txt_tamañoFila = Entry(datos, textvariable=entrada_fila, font=("Arial", 20)).place(x=450, y=250)

lb_tamañoColumna = Label(datos, text = "Tamaño Columna", bg = "SpringGreen3", fg = "Black", font=("Arial", 25)).place(x=800, y=200)
txt_tamañoColumna = Entry(datos, textvariable=entrada_columna, font=("Arial", 20)).place(x=800, y=250)

lb_partida = Label(datos, text = "Nombre Partida", bg = "SpringGreen3", fg = "Black", font=("Arial", 25)).place(x=625, y=290)
txt_partida = Entry(datos, textvariable=entrada_partida, font=("Arial", 20)).place(x=625, y=340)

bt_aceptar = Button(datos, text="Aceptar", bg ="dark green", font=("Arial", 25), command = lambda:cambiar(matriz)).place(x=625, y=440)
bt_cancelar = Button(datos, text="Cancelar", bg ="dark green", font=("Arial", 25), command =lambda:cambiar(inicio)).place(x=800, y=440)



#==================Frame 3 code
frame3_title=  tk.Label(matriz, text='',font='times 35', bg='SpringGreen3')
frame3_title.pack(fill='both', expand=True)

frame3_btn = tk.Button(matriz, text='Enter',command=lambda:cambiar(inicio))
frame3_btn.pack(fill='x',ipady=15)

fil = entrada_fila.get()
col = entrada_columna.get()

nfil = 1 / fil
ncol = 1 / col

f1 = Frame(matriz)
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


cambiar(inicio)

window.mainloop()