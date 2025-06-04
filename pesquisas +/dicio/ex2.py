import random

i = 0
dicio = {}
lista = []

while i < 4:
    dicio['nome'] = input("Nome do jogador: ")
    dicio['dado'] = random.randint(1,6)
    lista.append(dicio.copy())
    i += 1
print(lista)

for i in lista:
    maior = max(dicio['dado'])
    print(maior)