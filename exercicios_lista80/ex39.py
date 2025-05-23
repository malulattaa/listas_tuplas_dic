""" 
Fa¸ca a uni˜ ao de duas listas sem usar o operador +
"""
lista1 = []
lista2 = []
while True:
    l1 = input("Digite elementos para a lista 1 ou (sair) para encerrar: ").lower()
    if l1 == 'sair':
        break
    lista1.append(l1)
while True:
    l2 = input("Digite elementos para a lista 2 ou (sair) para encerrar: ").lower()
    if l2 == 'sair':
        break
    lista2.append(l2)

lista1.extend(lista2)
print(f"Listas juntas: {lista1}")

""" 
ZIP:
O que faz: Junta duas (ou mais) listas, combinando elemento a elemento em pares (tuplas).

Resultado: Uma sequência de tuplas, cada uma contendo um elemento de cada lista na mesma posição.

Exemplo:

lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]

resultado = list(zip(lista1, lista2))
print(resultado)  # [('a', 1), ('b', 2), ('c', 3)]

EXTEND:
O que faz: Adiciona todos os elementos de uma lista ao final de outra lista.

Resultado: Uma única lista com todos os elementos, concatenados.

exemplo:
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]

lista1.extend(lista2)
print(lista1)  # ['a', 'b', 'c', 1, 2, 3]

"""