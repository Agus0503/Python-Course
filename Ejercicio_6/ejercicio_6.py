'''Enunciado del ejercicio:
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
Color
Ruedas
Puertas
Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
Velocidad
Cilindrada
Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.'''

class Vehiculo():
    
     def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

# Creo un objeto de la clase Coche
mi_coche = Coche("Negro", 4, 4, 180, 1500)

# Muestreo de datos del objeto de la clase Coche 
print("Color del coche:", mi_coche.color)
print("Número de ruedas del coche:", mi_coche.ruedas)
print("Número de puertas del coche:", mi_coche.puertas)
print("Velocidad del coche:", mi_coche.velocidad)
print("Cilindrada del coche:", mi_coche.cilindrada)