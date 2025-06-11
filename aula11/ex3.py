# Exercício 3: Somar os quadrados dos números que são multiplos de 3
from functools import reduce
from random import randint

numeros = [randint(1,50) for _ in range(10)]
print(numeros)
mult_3 = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, numeros)))
print(mult_3)