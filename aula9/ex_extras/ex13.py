def soma_quadrados(lista):
    soma = 0
    resultado = sum([x ** 2 for x in lista])
    return resultado

print(soma_quadrados([2, 3]))
"""Objetivo: Retornar a soma dos quadrados dos números da lista"""