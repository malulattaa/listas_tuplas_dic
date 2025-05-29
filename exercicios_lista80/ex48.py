""" 
Dada uma lista de n´ umeros, retorne uma nova lista com os elementos ao quadrado,
mas somente os pares
"""
lista = []
while True:
    num = int(input("Digite números ou '000' para sair: "))
    
    if num == 000:
        break
    lista.append(num)
    
quadrado = [i**2 for i in lista if i % 2 == 0]
print(quadrado)