#map TRANSFORMA e retorna um novo array
#filter APLICA ALGUMA CONDIÇÃO E TE RETORNA OUTRO ARRAY COM BASE NUM CONDICIONAL

#REDUCE
""" 
aplica um func de 2 arg cumulativamente aos itens de um iteravel
reduz o iteravel a um unico valor
pega uma lista e aplica algum tipo de funcao e da um unico valor
é feita de forma acumulativa

pra usar reduce tem que fazer import
from functools import reduce
SINTAXE
reduce(func, array)
reduce(func, array, pode por opcional um inicializador aq)

geralmente filter, map e reduce estao combinadas
"""
from functools import reduce
from random import randint
numeros = [1, 2, 3, 4, 5, 6, 7]
#x variavel soma
#y corrente da lista
#x comeca com 0
#y vale 1
#x agr vale 1
#y vale 2
#x vale 3
#y vale 3 e por ai vai
soma_total = reduce(lambda x, y: x + y, numeros)
print(soma_total)


#outro exemplo
numeros = [randint(1,50) for _ in range(10)]


maior = reduce(lambda x,y: x if x > y else y, numeros)
print(maior)

# Exercicio 1: Calcular a media dos quadrados dos numeros pares de uma lista
# filter pra par
# elevar map
# media reduce

#correcao
media = reduce(lambda x, y: x + y, map(lambda x: x**2 ,filter(lambda x: x % 2 == 0, numeros))) / len(list(filter(lambda x: x % 2 == 0, numeros)))
print(media)

# Exercício 2: Encontrar o maior número impar após elevar ao cubo

# Exercício 3: Somar os quadrados dos números que são multiplos de 3

# Exercício 4: Calcular o produto dos números pares após multiplicar por 2

# Exercício 5: Encontrar a média dos números que são maiores que 5 após elevar ao quadrado

# Exercício 6: Calcular a soma dos cubos dos números que são menores que a média da lista