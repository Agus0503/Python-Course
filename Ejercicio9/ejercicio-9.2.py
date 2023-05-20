'''
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares
de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos 
obtenidos mediante reduce.
'''

from functools import reduce

lista = [1, 3, 5, 7, 9, 11, 13, 17, 19]

def impares(lista):
    return list(filter(lambda x: x % 2!= 0, lista))

def suma_impares(lista):
    return reduce(lambda x, y: x + y, impares(lista))