""" 
MEDIO

Solicite ao usu´ ario 10 n´ umeros, armazene em uma lista e remova todos os n´ umeros
pares usando remove.

"""

lista = []
i = 0
while i < 10:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    i += 1
print(f"Lista completa: {lista}")
for j in lista[:]: #o for percorre a cópia, mas o remove percorre a original
    if j % 2 == 0:
        par = j
        lista.remove(par)
        
print(f"Lista sem os pares: {lista}")
