'''En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.'''

archivo = open("ejercicio_8.1.txt", "w")
archivo.write("Hola, OpenBootcamp!")
archivo.close()

archivo = open("ejercicio_8.1.txt", "r")
contenido = archivo.read()
archivo.close()

print(contenido)  
