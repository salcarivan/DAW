#|Escribir una función eliminar_duplicados(lista) que reciba una lista de elementos
#y la modifique eliminando los elementos repetidos, de forma que sólo aparezcan una
#vez, en el mismo orden en el que aparecen en la lista.
#Ejemplo:
#>>> datos = [1, 2, 4, 3, 2, 4, 5, 6, 2]
#>>> eliminar_duplicados(datos)
#>>> print(datos)
#[1, 2, 4, 3, 5, 6]

lista = [1, 2, 4, 3, 2, 4, 5, 6, 2]

def eliminar_duplicados (lista) -> None:
    i=0
    while i < len(lista):
        j = i+1
        while j< len (lista):
            if lista[j] == lista [i]:
                del lista[j]
        else:
            j+=1
        i += 1
"""
Escribir una función analizar_diagonales(matriz) que reciba una lista de listas de
números, de forma que:
Si la matriz está vacía o no es cuadrada (es decir, alguna fila no tiene la misma
longitud que el número total de filas), debe devolver None.
Si es cuadrada, debe devolver una tupla (suma principal, suma secundaria) con la
suma de su diagonal principal y su diagonal secundaria"""
def es_cuadradada (matriz: list[list[int]])-> bool:
    num_filas = len(matriz)
    i= 0
    while i < num_filas:
        num_columnas =len(matriz[i])
        if num_columnas != num_filas:
            return False
        i+=1
    return True
def analiza__diagonales (matriz: list[list[int]])-> None | tuple[int, int]:
    if matriz == [] or not es_cuadradada(matriz): 
        return False
    suma_pricipal, suma_secundaria = 0,0
    i= 0
    while i< len(matriz):
        suma_pricipal += matriz[i][i]
        suma_secundaria+= matriz[i][- 1 - i]
        i +=1
    return (suma_pricipal, suma_secundaria)

analiza__diagonales([[4,8,3],[2,6,5],[1,9,7]])
