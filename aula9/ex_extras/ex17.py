"""Crie a função media_multiplos_de_4(lista) que:

retorna a média dos números múltiplos de 4 da lista

Se não houver nenhum múltiplo de 4, retorna 0 sem erro"""

def media_multiplos_de_4(lista):
    media = sum([x for x in lista if x % 4 == 0]) / len([x for x in lista if x % 4 == 0]) if any(x % 4 == 0 for x in lista) else 0
    return(media)
    
    
print(media_multiplos_de_4([14,24,13,78,24,45,16,12]))