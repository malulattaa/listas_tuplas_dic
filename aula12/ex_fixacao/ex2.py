""" 
Faça uma função recursiva que conte quantos caracteres há em uma string (sem usar len).
Ex: contar("maria") → 5
"""

def caractere(string):
    if len(string) <= 0:
        return 0
    return 1 + caractere(string[1:]) 

print(caractere("maria"))