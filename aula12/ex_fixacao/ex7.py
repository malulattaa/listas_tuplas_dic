""" 
Crie uma função recursiva que receba uma lista de inteiros e devolva a soma de todos os elementos.
"""

def soma(elementos):
    if len(elementos) <= 1:
        return 1
    return elementos[-1] + soma(elementos[:-1])
    
print(soma([1,2,3,4]))