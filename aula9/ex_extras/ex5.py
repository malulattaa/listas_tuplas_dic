def gerar_numeros(n):
    return [n, n+1, n+2, n+3, n+4]
#3, 4, 5, 6, 7

def filtrar_pares(lista):
    return [x for x in lista if x % 2 == 0]
#4,6
def resultado(n):
    return filtrar_pares(gerar_numeros(n))

# Teste
print(resultado(3))
"""Pergunta:
O que o código está filtrando? Por que?

os numeros pares, pq ele pega a lista de gerar numeros e faz um if x % 2 == 0 onde x é cada num da lista


"""

