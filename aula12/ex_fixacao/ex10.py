""" 
Dada uma lista e um número x, retorne quantas vezes x aparece.
"""

def aparicao(lista, n):
    if len(lista)==0:
        return 0
    contagem = 1 if lista[-1] == n else 0
    return contagem + aparicao(lista[:-1], n)

print(aparicao([1,2,3,2,5,2], 2))