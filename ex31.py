"""Crie uma fun¸ c˜ao que verifique se uma lista est´a ordenada"""

#sorted: serve para ordenar, nesse caso ele esta comparando a lista, com a versão ordenada dela

lista = []

while True:
    num = int(input("Digite números para saber se estão ordenados ou (0) para sair: "))
    if num == 0:
        break
    lista.append(num)
    
def ordenada(lista):
    if lista == sorted(lista):
        print("A lista está ordenada")
    else:
        print("A lista não está ordenada")
    return lista
print(ordenada(lista))