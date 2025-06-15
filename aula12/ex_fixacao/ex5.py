""" 
Implemente uma função recursiva que imprima uma contagem de um número até 0.

"""

def contagem(n):
    if n < 1:
        return 0 
    return n, contagem(n-1)

print(contagem(10))

def contagem(n):
    if n < 1:
        return 0 
    print(n)
    contagem(n-1)

(contagem(10))