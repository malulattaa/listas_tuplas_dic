""" 
Objetivo: Dado uma lista de números, retorne a soma dos quadrados dos números positivos.
"""

def quadrado(n):
    quadrados = [x**2 for x in n if x > 0]
    return quadrados

def somar_quadrados_positivos(lista):
    soma = sum(x for x in quadrado(lista))
    return soma
    
print(somar_quadrados_positivos([-6, 4, 5, -2, -5, 3]))