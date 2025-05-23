""" 
É uma forma rápida e prática de criar listas em Python, usando uma sintaxe compacta

ESTRUTURA:
[nova_expressao for item in iterável if condição]

nova_expressao: o que você quer adicionar à lista

item: cada elemento do iterável (exemplo: uma lista, range, etc)

condição (opcional): filtra quais elementos serão incluídos

ex:
quadrados = [i ** 2 for i in range(1, 6)]
print(quadrados)
# Saída: [1, 4, 9, 16, 25]


ex com cond:
pares_quadrados = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(pares_quadrados)
# Saída: [4, 16, 36, 64, 100]

"""

lista = [i for i in range(5)] 
# Resultado: [0, 1, 2, 3, 4]


lista = [i**2 for i in range(5)] 
# Resultado: [0, 1, 4, 9, 16]


#A sintaxe correta de listas de compreensão com dois for:
    #lista = [resultado for x in range(...) for y in range(...) if condicao]
