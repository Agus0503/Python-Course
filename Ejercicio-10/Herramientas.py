# ---------- GUI -------------
#PyQt
#Tkinter -> TCL=Lenguaje de programacion(integracion con tool kits para GUI)
import tkinter #Genera un codigo TCL
from tkinter import ttk
#Componente = Botones,checkbox,etc -> Siempre dentro de un contenedor(frames o ventanas)

#Crear ventanas -> Necesito un loop para que no solo ejecute, sino tambien mantenga mi ventana para visualizarla
window = tkinter.Tk()


'''GEOMETRIA PACK'''

#Crear componente
#label_saludo = tkinter.Label(window,text= "Bienvenido",bg= "Red",fg="Grey") #Esta creado NO mostrado

#Geometria "Pack"(Agrupar)
#label_saludo.pack(ipadx=50,ipady=50,fill='x') #Esta mostrado
'''
-fill = 'x' -> ocupa todo el horizontal
-fill = 'y' -> ocupa todo el vertical
-fill = 'both' -> ocupa todo el horizontal y vertical
-Teniendo en cuenta los parametros ipadx e ipady, puedo no ingresar
ipadx e ipady y solo ocupara un segmento de la ventana
-Si utilizo solo fill = 'both' y expand = True ocupa un segmento que se expandira proporcionalmente a la ventana
en su espacio designado
- Puedo colocar como argumeno side = 'left' / 'right' para ubicar el label segun se desea
'''

#label_saludar = tkinter.Label(window,text= "Adios",bg= "Red",fg="Grey")
#label_saludar.pack(ipadx=50,ipady=50) #Esta mostrado


'''GEOMETRIA GRID'''

#window.columnconfigure(0,weight=1)
#window.rowconfigure(1,weight=3)

# username_label = ttk.Label(window,text= "Username: ")
# username_label.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)
#El argumento sticky=tkinter.W permite fijar en un solo lugar(izq del todo)
#Pero si lo cambio por sticky=tkinter.E, se va a la derecha del todo
# password_label = ttk.Label(window,text= "Password: ")
# password_label.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

#--------------------------------------------------------------------------

#Crear inputbox
# username_entry = ttk.Entry(window)
# username_entry.grid(column=1,row=0,sticky=tkinter.W,padx=5,pady=5)

# password_entry = ttk.Entry(window,show='*')
# password_entry.grid(column=1,row=1,sticky=tkinter.W,padx=5,pady=5)

#Crear boton
# login_button = ttk.Button(window,text="Login")
# login_button.grid(column=1,row=3,sticky=tkinter.E,padx=5,pady=5)


'''GEOMETRIA PLACE -> Posicionar de forma absoluta o relativa'''

#label1 = tkinter.Label(window,text="Posicionamiento Absoluto",bg="blue",fg="white")
#label1.place(x=10,y=50)

#label2 = tkinter.Label(window,text="Posicionamiento Absoluto",bg="blue",fg="white")
#label2.place(relx=10,rely=15,relwidth=0.5,anchor='ne')


'''LISTBOX'''

#lista = ["Windows","Linux","Mac","OS/2"]
#lista_items = tkinter.StringVar(value=lista)
#listbox = tkinter.Listbox(window,height=100,listvariable=lista_items)
#listbox.grid(column=0,row=1,sticky=tkinter.W)

'''RADIOBUTTON'''

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window,text='Si',value='1',variable=selected)
r2 = ttk.Radiobutton(window,text='No',value='2',variable=selected)
r3 = ttk.Radiobutton(window,text='Nose',value='3',variable=selected)

r1.grid(column=0,row=1,padx=5,pady=5)
r2.grid(column=0,row=2,padx=5,pady=5)
r3.grid(column=0,row=3,padx=5,pady=5)

'''CHECKBOX'''
#selected = tkinter.StringVar()
#checkbox = ttk.Checkbutton(window,text='Aceptar terminos y condiciones',variable=selected)
#checkbox.grid(column=0,row=0)

'''EVENTOS'''
# def saludar(event):
#     print("ATR")

# def saludar_doble_clik(event):
#     print("ATR mas piola")

#boton = tkinter.Button(window,text='click aca')
#boton.pack()
#boton.bind('<Button-1>',saludar)
#boton.bind('<Double-1>',saludar_doble_clik)

'''BOTON DE SALIR'''
# def salir(event):
#     print("Adios")
#     window.quit()

# boton_salir = tkinter.Button(window,text='Salir')
# boton_salir.pack()
# boton_salir.bind('<Button-1>',salir)


#Creacion del loop
window.mainloop()

""" 
CTRL + KC - COMENTAR 
CTRL + KU - DESCOMENTAR
"""