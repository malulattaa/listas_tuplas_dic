""" 
 Implemente uma fun¸ c˜ao que gire os elementos de uma lista N posi¸c˜ oes para a direita
"""

#len
#lista[j], lista[j+1]

#para a direita
def girar(giro, lista):
    if giro <= 0:
        return lista
    #recursividade, giro -1?
    ultimo = lista[-1]
    resto = lista[:-1]
    return girar(giro -1, [ultimo] + resto)

lista = [1, 2, 3, 4, 5, 6]

giro = int(input("Deseja girar a lista para a direita quantas vezes? "))
girada = girar(giro, lista)
print(girada)

#para esquerda
def girar_esquerda(giro, lista):
    if giro <= 0:
        return lista
    primeiro = lista[0]
    resto = lista[1:]
    return girar_esquerda(giro - 1, resto + [primeiro])

lista = [1, 2, 3, 4, 5, 6]

giro = int(input("Deseja girar a lista para a direita quantas vezes? "))
girada = girar_esquerda(giro, lista)
print(girada)