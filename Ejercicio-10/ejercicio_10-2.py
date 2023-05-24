'''
En este segundo ejercicio, tendréis que crear una interfaz sencilla
la cual debe de contener una lista de elementos seleccionables, también 
debe de tener un label con el texto que queráis.
'''

import tkinter

window = tkinter.Tk()

label_seleccion = tkinter.Label(window, text="Elija su SO", bg="Black", fg="White")
label_seleccion.pack(ipadx=50, ipady=50, fill='x')

lista = ["Windows", "Linux", "Mac", "OS/2"]
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, listvariable=lista_items)
listbox.pack()

window.mainloop()
