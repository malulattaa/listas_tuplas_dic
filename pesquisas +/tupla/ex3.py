import random
lista = []

for i in range(0,5):
    num = random.randint(0,100)
    lista.append(num)

tupla = tuple(lista)
print(tupla)

maior = max(tupla)
print(f"Maior: {maior}")
menor = min(tupla)
print(f"Menor: {menor}")