""" 
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
a. quantas vezes apareceu o valor 9
b. em que posição foi digitado o primeiro valor 3
c. quais foram os numeros pares
"""

lista = []

for i in range(0,5):
    num = int(input("Digite um número: "))
    lista.append(num)

tupla = tuple(lista)
print(tupla)

print("")

print(f'O número 9 apareceu: {tupla.count(9)} vezes' )

print("")


for i in tupla:
    if i % 2 == 0:
        print(f"pares: {i}")
        
print("")

if 3 in tupla:
    print(f"O número 3 foi digitado pela primeira vez na posição {tupla.index(3)}")
else:
    print(" 3 não foi digitado")



