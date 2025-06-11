# Exercício 4: Calcular o produto dos números pares após multiplicar por 2

from functools import reduce
from random import randint

numeros = [randint(1,50) for _ in range(10)]
print(numeros)

produto = reduce(lambda x, y: x*y, map(lambda x: x*2, filter(lambda x: x % 2 == 0, numeros)))
print(produto)