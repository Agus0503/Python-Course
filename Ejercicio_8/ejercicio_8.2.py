'''En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
   haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.'''

import csv

class Vehículo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

mi_coche = Vehículo("Ford", "Falcon", 1995)

with open("Ejercicio_8.2.Csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow([mi_coche.marca, mi_coche.modelo, mi_coche.año])
    
with open("Ejercicio_8.2.Csv", "r") as archivo:
    lector = csv.reader(archivo)
    mi_coche_lista_cargada = list(lector)[0]

mi_coche_cargado = Vehículo(mi_coche_lista_cargada[0], mi_coche_lista_cargada[1], int(mi_coche_lista_cargada[2]))