'''
Crea un script que le pida al usuario una lista de países (separados por comas).
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados 
por comas.
'''

lista_paises = []

def obtener_lista_paises():

    paises = input("Ingrese una lista de países separados por comas: ")
    if " " not in paises:
        lista_paises = [pais.strip() for pais in paises.split(",")]
        paises_unicos = list(set(lista_paises))
        paises_unicos.sort()
    else:
        paises_unicos = None

    return paises_unicos

lista_paises = obtener_lista_paises()

if lista_paises:
    paises_ordenados = ", ".join(lista_paises)
    print("Lista de países ordenados alfabéticamente:")
    print(paises_ordenados)
else:
    print("Error en la carga de datos")
