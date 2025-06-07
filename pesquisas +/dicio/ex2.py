import random
from time import sleep
from operator import itemgetter
i = 0
dicio = {}
lista = []

while i < 4:
    nome = input("Nome do jogador: ")
    dicio[nome] = random.randint(1,6)
    lista.append(dicio.copy())
    i += 1
print(lista)
ranking = []
for k,v in dicio.items():
    print(f"{k} tirou {v}")
    sleep(1)
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
#no 1 pq ai ele pega os valores e nao chaves