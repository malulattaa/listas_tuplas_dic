""" 
Escreva uma função recursiva que inverta os elementos de uma lista.
"""


def inverter(n):
    if len(n) <= 1:
        return n
    return [n[-1]] + inverter(n[:-1])

print(inverter([1,5,2,9,4,5,6]))
    