""" 
Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a
ordem
"""

nomes = ['maria', 'luisa', 'maria', 'gabi' , 'luisa', 'matheus','gabi']

sem_repetidos = list(dict.fromkeys(nomes))
print(sem_repetidos)  

""" 
dict.fromkeys remove elementos duplicados de uma lista preservando a ordem.
Cria um dicionário onde as chaves são os elementos da lista nomes.

Dicionários não permitem chaves repetidas, então os duplicados são descartados.

A ordem dos primeiros elementos únicos é mantida

dps tranforma dnv em lista
"""