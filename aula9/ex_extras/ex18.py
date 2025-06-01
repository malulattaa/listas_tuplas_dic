"""Crie uma função filtrar_positivos(lista) que:

retorna uma nova lista com apenas os valores maiores que zero

"""
def filtrar_positivos(lista):
    positivos = [x for x in lista if x >0]
    return positivos
print(filtrar_positivos([-2, 0, 3, 5, -1]))