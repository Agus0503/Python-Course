'''
En este ejercicio tenéis que crear una lista de RadioButton 
que muestre la opción que se ha seleccionado y que contenga un
botón de reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.
'''

import tkinter
from tkinter import ttk

window = tkinter.Tk()

selected = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='Si', value='1', variable=selected)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
r3 = ttk.Radiobutton(window, text='Nose', value='3', variable=selected)
reset = ttk.Button(window, text='Reset', command=lambda: selected.set(""))

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)
reset.grid(column=0, row=4, padx=5, pady=5)

window.mainloop()
