""" Crie uma lista de listas representando uma matriz 3x3 e some os valores de cada
linha.

"""

matriz = []

for r in range(3):
    nums = input("Digite 3 números separados por espaço: ")
    nums_int = list(map(int, nums.split()))
    matriz.append(nums_int)
    
for linha in matriz:
    print(linha)
    print(f"Soma da linha: {sum(linha)}")
    