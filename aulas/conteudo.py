"""
listas; tuplas; dicionarios

listas sao coleções heterogeneas de objetos, podem ser qualquer tipo, inclusive outras listas

[0, 1, 10, "beto", [0.2, 0.3]]

são mutaveis, modificar, retirar, fatiar e adiconar elementos na lista 

vetor nao existe na programação, o que existe é uma classe chamada vector e a partir disso ele existe
"""

lista = [1, 2, 3, 4, 5]

print(lista[4])

nome = "maria"

print(nome[2])

#len: função que retorna o tamanho de uma coleção
print(len(nome))

progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']
#Isso é uma lista de listas, ja que string é uma lista e esta dentro de uma lista

"""
print(progs[0])
print(progs[1])
print(progs[2])
print(progs[3])
"""
#isso so pode usar para imprimir a posição em especifico, mas nao a lista inteira

progs[3]= 'metalica'

# primeira forma de varrer uma lista
for i in range (4):
    print(progs[i])
#isso nao é mt eficiente pq a lista pd crescer a qlq momento e aqui ta limitado a um num especifico
#necessita dos colchetes para imprimir elemento por elemento
for i in range(len(progs)):
    print(progs[i])

#IMPRIMINDO LETRA POR LETRA:

for prog in progs:
    for letra in prog:
        print(letra, end="")
        
# segunda forma

for prog in progs:
    print(prog)

#incluindo novo elemento

progs.append("nao sei")
#append insere sempre no final

#para inserir um elemento sem ser no final:
    #insert(posição, valor) → adiciona na posição especificada
#trocar o ultimo elemento
progs[-1] = "novo elemento"
#lista[indice] = novo_valor serve para substituir qualquer elemento

""" 
Índices negativos são úteis quando você quer 
acessar os últimos elementos, mesmo sem saber o tamanho da lista. Por exemplo, para substituir o último item sem usar len(progs) - 1.

"""

#ordenar
progs.sort()

#inverter a lista
progs.reverse()

#PESQUISA
#pop
#remove

props = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']

#i é o indice e p é o elemento (pesquisar pq tem mais, mas ele n vai cobrar)
for i, p in enumerate(props):
    print(f"Posição {i} e elemento = {p}")
#pesquisar outras formas(pop, remove, remote, zip (ver pra oq serve, como utilizar, restrições e caso de uso))
#dada as seguintes listas [A, B, C] e [D, E, F] como poderiamos juntar?

""" 
TUPLASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
semelhantes as listas e imutaveis: não acrescenta, não apaga e não faz atribuição
mais eficientes
"""
#oq determina que é uma tupla são as virgulas, elas podem ser utilizadas sem parenteses, mas por convensão são usados
tupla = (1, 2, 3, 4)

#tupla de um unico elemento
t1 = (1,)
#acessar
print(t1[0])

#ou

for t in tupla:
    print(t)
    
#como transformar uma tupla em uma lista
    #percorrer a tupla e colocar os elementos em uma nova lista
    #ou

lista = list(tupla)

#tupla de listas

lt = ([1, 2, 3], [2, 3], ['beto', 'maria', 'luisa'])

#pesquisa
#set (forma de aplicação e todo o resto)
#frozenset (se é imutavel, mutavel, ordenado ou nao e etc)


#ter conhecimento sobre união, interseção e diferença (importante para lista)

#o que é range? função que pode se assemelhar a um tipo de lista ou tupla (?)