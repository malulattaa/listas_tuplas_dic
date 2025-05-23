"""Leia 5 n´ umeros do usu´ ario e verifique se cada um deles ´ e maior que 10"""

i = 0
numeros = []

while i < 5:
    n = int(input("Digite um número: "))
    numeros.append(n)
    i+=1
    
for j in range(len(numeros)):
    if numeros[j]>10:
        print(f"{numeros[j]} é maior que 10")
    else:
        print(f"{numeros[j]} é menor que 10")