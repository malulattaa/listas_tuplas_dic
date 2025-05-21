lista = []
pares = []

for i in range(1,11):
    lista.append(i)

for j in range(len(lista)):
    if lista[j] % 2 == 0:
        pares.append(lista[j])
print(pares)