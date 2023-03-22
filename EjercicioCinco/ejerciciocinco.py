#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def esBisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                 print(f"El año {anio} es bisiesto")
            else:
                print(f"El año {anio} NO es bisiesto")
        else:
            print(f"El año {anio} es bisiesto")
    else:
            
       print(f"El año {anio} NO es bisiesto")
        
        
esBisiesto(2019)