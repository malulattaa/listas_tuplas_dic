# Exercício 5: Encontrar a média dos números que são maiores que 5 após elevar ao quadrado

from functools import reduce
from random import randint

numeros = [randint(1,50) for _ in range(10)]
print(numeros)


media = reduce(lambda x,y: x+ y, filter(lambda x: x > 5, map(lambda x: x**2, numeros))) / len(list(filter(lambda x: x > 5, numeros)))
print(media)