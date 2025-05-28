lista = []

for i in range(0,5):
    num = int(input("Digite um número: "))
    lista.append(num)

tupla = tuple(lista)
print(tupla)
for i in tupla:
    if i % 2 == 0:
        print("Números pares: ", end="")
        print(i)
if 3 in tupla:
    print(f"O número 3 foi digitado pela primeira vez na posição {tupla.index(3)}")
else:
    print(" 3 não foi digitado")

print(f'O número 9 apareceu: {tupla.count(9)} vezes' )


