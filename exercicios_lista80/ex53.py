""" 
Implemente a busca binaria em uma lista ordenada.
"""

def binaria(lista, n, inicio, fim):
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == n:
        return meio
    
    if lista[meio] < n:
        return binaria(lista, n, meio + 1, fim)
    else:
        return binaria(lista, n, inicio, meio - 1)
    
lista = [2, 6, 8, 12, 15, 18, 22, 28]
n = int(input("Número buscado: "))
busca = binaria(lista, n, 0, len(lista)-1)
if busca != -1:
    print(f"O número {n} está na {busca+1}° posição")
else:
    print("O número não está na lista")