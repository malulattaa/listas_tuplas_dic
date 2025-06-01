def contar_maiores_que_10(lista):
    resultado = len([x for x in lista if x > 10])
    return resultado

print(contar_maiores_que_10([5, 11, 20, 8, 10]))
"""Objetivo: Retornar quantos números são maiores que 10."""