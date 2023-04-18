'''En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado 
de la nota y si ha aprobado o no.'''

class Alumno():
    
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_informacion(self):
        print("Nombre del alumno:", self.nombre)
        print("Nota:", self.nota)
    
    def verificar_aprobacion(self):
        if self.nota >= 6:
            print(f"El alumno {self.nombre} esta Aprobado")
        else:
            print(f"El alumno {self.nombre} esta Desaprobado")
    

alumno1 = Alumno("Pepe", 5)
alumno1.mostrar_informacion()
alumno1.verificar_aprobacion()

alumno2 = Alumno("Rodrigo", 7)
alumno2.mostrar_informacion()
alumno2.verificar_aprobacion()