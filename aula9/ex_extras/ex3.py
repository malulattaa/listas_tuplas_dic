def gerar_lista(n):
    return [n, n + 1, n + 2]
    #2, 3, 4

def elevar_quadrado(lista):
    return [x**2 for x in lista]
#4, 9, 16

def resultado(n):
    #parametro = 2
    return elevar_quadrado(gerar_lista(n))

# Teste
print(resultado(2))
"""Pergunta:
O que é impresso? Qual é a ordem das chamadas?

4, 9, 16. 

reultado recebe 2 como parametro, e retorna gerar_lista(2). gerar_lista retorna 2, 2+1 e 2+2. agr ainda em resultadom elevar ao quadrado recebe
gerar_lista como parametro e ele cada um ao quadrado.
"""