

def bubble(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista [j+1]:
                segundo = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = segundo
    return lista

lista = [35, 5, 44, 16, 25, 11,4]
print(bubble(lista))
#se o primeiro cara for maior que o segundo
#substitui o segundo pelo valor do primeiro
#antes tem que armazenar o valor do segundo
#depois o primeiro pega o valor do segundol