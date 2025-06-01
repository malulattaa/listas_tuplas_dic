"""Crie a função soma_condicional(lista) que:

soma apenas os números positivos e múltiplos de 5"""

def soma_condicional(lista): 
    soma = sum([x for x in lista if x % 5 == 0 and x > 0])
    return soma

print(soma_condicional([1,5,-10,0,9,-15,15]))