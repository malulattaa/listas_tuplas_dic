""" 
Crie a função quadrado_impares(lista) que:

retorna uma lista com o quadrado de todos os valores ímpares

"""

def quadrado_impares(lista):
    quadrado = [x**2 for x in lista if x % 2 != 0]
    return quadrado

print(quadrado_impares([2,3,5,8,11]))