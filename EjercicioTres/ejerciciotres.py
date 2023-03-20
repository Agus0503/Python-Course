peso = float(input("Por favor, ingresa tu peso en kg: "))
estatura = float(input("Por favor, ingresa tu estatura en metros: "))

imc = peso / (estatura ** 2) # Calcula el índice de masa corporal

imc_redondeado = round(imc, 2) # Redondea el resultado a dos decimales

print("Tu índice de masa corporal es", imc_redondeado)