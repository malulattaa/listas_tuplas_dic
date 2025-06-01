def soma_lista(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma

def gerar_lista(n):
    return [n, n + 2, n + 4]
#3, 5, 7

print(soma_lista(gerar_lista(3)))


