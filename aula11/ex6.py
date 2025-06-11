# Exercício 6: Calcular a soma dos cubos dos números que são menores que a média da lista

from functools import reduce
from random import randint

numeros = [randint(1,50) for _ in range(10)]
print(numeros)

#media da lista
media_lista = reduce(lambda x,y: x+y, map(lambda x: x**3, filter(lambda x: x < (reduce(lambda x,y: x + y, numeros) / len(numeros)), numeros)))
print(media_lista)
