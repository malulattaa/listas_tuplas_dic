""" 
Faça uma função recursiva que receba uma lista e retorne o maior valor.
"""

def maior(valor):
    if len(valor) <= 1:
        return valor[0]
    return max(valor[-1], maior(valor[:-1]))

print(maior([4,5,8,6,2]))