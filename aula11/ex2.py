# Exercício 2: Encontrar o maior número impar após elevar ao cubo
from functools import reduce
from random import randint
numeros = [randint(1,50) for _ in range(10)]

print(numeros)
maior_impar = reduce(lambda x,y: x if x > y else y, filter(lambda x: x % 2 != 0, map(lambda x: x**3, numeros)))
print(maior_impar)