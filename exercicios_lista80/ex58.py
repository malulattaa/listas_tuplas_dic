""" 
Dada uma lista de n´umeros, encontre a subsequˆencia crescente mais longa.
"""

lista = [3, 1, 2, 5, 4, 6]
sub = []
for n in range(len(lista)-1):
    if lista[n] < lista[n+1]:
        sub.append(n)
    elif lista[-1] > lista[-2]:
        sub.append(lista[-1])
print(sub)