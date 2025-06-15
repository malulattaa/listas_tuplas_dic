""" 
Crie uma função recursiva que receba um número n e retorne a soma dos números de 1 até n.
Ex: soma(5) → 1 + 2 + 3 + 4 + 5 = 15

"""

def retornar(n):
    if n<= 0:
        return 0
    return n + retornar(n-1)

print(retornar(5))