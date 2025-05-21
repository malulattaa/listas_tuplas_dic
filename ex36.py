import random
"""Crie uma fun¸ c˜ao que retorne o segundo maior n´ umero de uma lista."""
numeros = []
for i in range(20):
    num = random.randint(0,100)
    numeros.append(num)
print(numeros)
def segundo_maior(numeros):
    maior = max(numeros)
    numeros.remove(maior)
    maior2 = max(numeros)
    return (maior2)

print(segundo_maior(numeros))