def contar_pares(lista):
    resultado = len([i for i in lista if i % 2 == 0 ])
    """for i in range(len(lista)-1):
        if i % 2 == 0:
            resultado = i"""
    return resultado

print(contar_pares([1, 2, 3, 4, 5, 6, 8]))
"""Objetivo: Retornar quantos números pares existem na lista."""