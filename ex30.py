""" 
Dadaumalista de strings, crie uma nova lista com o tamanho (n´ umero de caracteres)
de cada string
"""

lista = ['maçã', 'banana', 'pêssego', 'uva']
qtde = []

for i in range(len(lista)):
    qtde.append(len(lista[i]))
    
print(qtde)
