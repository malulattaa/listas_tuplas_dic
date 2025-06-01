"""  
criando do zero: 


Crie uma função chamada soma_pares que:

recebe uma lista de números

retorna a soma de todos os números pares

"""
def soma_pares(lista):
    soma = sum([x for x in lista if x % 2 == 0])
    return soma
print(soma_pares([1, 2, 3, 4, 5]))  # retorna 6 (2 + 4)
