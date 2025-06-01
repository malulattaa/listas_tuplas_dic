def gerar_expoentes(n):
    return [n, n*2, n*3]
#3, 6, 9

def potencia_lista(lista):
    return [2 ** x for x in lista]
#2**3 = 8
#2**6 = 64
#2**9 = 512

def resultado(n):
    return potencia_lista(gerar_expoentes(n))

# Teste
print(resultado(3))
"""Pergunta:
Qual é a saída? Por que o 2 vem antes do x?

#2**3 = 8
#2**6 = 64
#2**9 = 512

pq ele quer elevar o dois a um nu da lista ué lkkk
"""