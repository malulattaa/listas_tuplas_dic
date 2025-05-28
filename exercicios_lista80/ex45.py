""" 
Fa¸ca uma fun¸c˜ ao que receba uma lista de listas e retorne uma lista ”achatada”(flatten).
"""

sublista = [[1, 2], [3, 4], [5]]

"""def flatten(sublista):
    resultado = []
    for lista in sublista:
        for i in lista:
            resultado.append(i)
    return resultado
    
print(flatten(sublista))"""


def flatten(sublista):
    lista = [item for listas in sublista for item in listas]
    return lista

print(flatten(sublista))