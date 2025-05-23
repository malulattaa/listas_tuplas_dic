numeros = []
i = 0
while i<5:
    add = int(input("Digite um número: "))
    numeros.append(add)
    i+=1

maior = numeros[0]
for j in numeros:
    if j>maior:
        maior = j
print(f"Maior número: {maior}")

menor = numeros[0]
for k in numeros:
    if k<menor:
        menor = k
print(f"Menor número: {menor}")
