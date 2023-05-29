'''
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
- la columna id de tipo entero
- la columna nombre que será de tipo texto
- la columna apellido que también será de tipo texto.
Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
'''

import sqlite3

def buscar_alumnos():
    
    nombre = input("Ingrese el nombre del alumno que desea encontrar: ")
    
    rows = cursor.execute('SELECT * FROM alumnos')

    alumno_encontrado = False

    for row in rows:
        for dato in row:
            if nombre == dato:
                print(row)
                alumno_encontrado = True
                break
    
    if not alumno_encontrado:
                print("Alumno no encontrado")
    
    return alumno_encontrado

conn = sqlite3.connect("Ejercicio-11/Alumnos.db")
cursor = conn.cursor()

buscar_alumnos()

cursor.close()
conn.close()


