""" 
Crie uma função que receba uma lista de inteiros e retorne a soma dos quadrados apenas dos números positivos.
"""

def quadrados_positivos(lista):
    soma = sum([x**2 for x in lista if x > 0])
    return soma
    
print(quadrados_positivos([2, 6, 9, 8,-2,-1,-6]))