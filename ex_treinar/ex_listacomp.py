""" 
Crie uma lista com os quadrados dos números de 0 a 5.
"""

quadrados = [i**2 for i in range(0,6)]
print(quadrados)


""" 
Crie uma lista com os números pares de 0 a 10.
"""

pares = [i for i in range(0,11) if i % 2 == 0]
print(pares)

""" 
Crie uma lista com o comprimento de cada palavra em ["maria", "python", "lista", "compreensao"].

"""
lista =  ["maria", "python", "lista", "compreensao"]
comp = [len(i) for i in lista]
print(comp)

""" 
Filtre de uma lista [1, 2, 3, 4, 5, 6, 7, 8] apenas os números maiores que 4 usando compreensão.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8]
maior = [i for i in lista if i > 4]
print(maior)