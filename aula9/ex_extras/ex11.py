def somar_impares(lista):
    resultado = sum([i for i in lista if i % 2 != 0])
    
    return resultado

print(somar_impares([1, 2, 3, 4, 5, 6]))


""" 
Somar apenas os números ímpares da lista.
"""