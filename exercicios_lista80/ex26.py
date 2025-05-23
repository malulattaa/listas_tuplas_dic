"""Inverta os elementos de uma lista sem usar o m´etodo reverse."""

lista = [1, 2, 3, 4, 5]

inverter = []

for i in range(len(lista)-1, -1, -1):
    inverter.append(lista[i])
print(inverter)



#outro

""" 
slicing: 
É uma forma de fatiar (pegar pedaços) de uma sequência usando a sintaxe:
sequencia[inicio:fim:passo]
inicio — índice onde começa (inclusive)

fim — índice onde termina (exclusivo)

passo — quantos elementos pula (pode ser negativo)

inicio: Posição onde começa (0 é o primeiro elemento).
Se deixar vazio, assume o começo da lista se o passo for positivo, ou o fim da lista se o passo for negativo.

fim: Posição onde termina (não inclui esse índice). -- EXCLUSIVOOOO
Se deixar vazio, assume o fim da lista se o passo for positivo, ou o começo da lista se o passo for negativo.

passo: Quanto pula a cada índice.
Pode ser positivo (vai para frente) ou negativo (vai para trás).


lista = [10, 20, 30, 40, 50]
print(lista[1:4])    # Pega do índice 1 até 3 → [20, 30, 40]
print(lista[:3])     # Pega do começo até índice 2 → [10, 20, 30]
print(lista[2:])     # Pega do índice 2 até o fim → [30, 40, 50]

invertendo = lista[::-1]
print(invertendo)
"""