""" 
Implemente a fun¸c˜ao zip manualmente (como em zip(lista1, lista2)).
"""

#relembrando zip

nomes = ['maria', 'matheus', 'luisa']
idades = [19, 18, 10]

juntas = list(zip(nomes, idades))
print(juntas)

#desempacotar

matriz = [
    
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    
]

desempac = list(zip(*matriz))
print(desempac)

#exercicio

lista1 = [int(input("Número: ")) for _ in range(3)]
lista2 = [int(input("Número: ")) for _ in range(3)]

lista1 += lista2
print(lista1)