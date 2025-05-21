from collections import Counter
""" Dadaumalista de inteiros, crie uma fun¸ c˜ao que identifique os n´ umeros que aparecem
mais de uma vez e quantas vezes cada um aparece

Counter é uma classe especial do Python que conta automaticamente quantas vezes cada valor aparece em uma lista.
counter é tipo {número: quantidade_de_vezes}
"""

numeros = []

while True:
    valor = int(input("Digite valores para a lista ou (0) para sair? "))
    if valor == 0:
        break
    numeros.append(valor)
def qtde(numeros):
    quantidade = Counter(numeros) #{2: 3, 5: 1, 9: 2} → ou seja, 2 aparece 3 vezes, 5 aparece 1 vez, etc.
    for n, cont in quantidade.items(): #O loop percorre cada número (n) e sua quantidade (cont)
        if cont > 1: 
            print(f"O número {n} aparece {cont} vezes")

qtde(numeros)
