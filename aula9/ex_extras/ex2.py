def quadrado(n):
    return n * n

def calcula(n):
    return quadrado(n + 1)

# Teste
print(calcula(3))


""" 
Explique a ordem de execução. Qual número é passado para quadrado?

o valor 3 é passado para a função calcula que recebe ele como parametro, retornando quadrado(3+1), ou seja, quadrado recebe 4 como parametro
quadrado(4) -> 4*4 = 16

"""