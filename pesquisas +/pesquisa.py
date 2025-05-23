""" 
PESQUISA
pop
remove
zip
tupla:
set (forma de aplicação e todo o resto)
frozenset (se é imutavel, mutavel, ordenado ou nao e etc)
ter conhecimento sobre união, interseção e diferença (importante para lista)
o que é range? função que pode se assemelhar a um tipo de lista ou tupla (?)
"""
#percorrendo lista de tupla
pares = [(1, 'um'), (2, 'dois')]
for numero, texto in pares:
    print(numero, texto)
    
    
#remove
""" 
ELEMENTO
remove a primeira ocorrência de um elemento na lista
ou seja, remove pelo VALOR DO ELEMENTO, não retorna o valor
se o valor indicado não existir ele retorna um valueError
"""
frutas = ["maçã", "banana", "uva", "pera", "pessego"]

frutas.remove("banana")
print(frutas)

#pop
"""
INDICE
remove E RETORNA o elemento em uma posição específica
remove pelo indice/posição, retorna o valor, se não existir, retorna indexError 
caso o índice nao seja passado, remove O ULTIMO ELEMENTO
"""

fruta_pop = frutas.pop(2)
print(frutas) #imprime sem pera
print(fruta_pop) #imprime o elemento removido (pera)

#sem indice
fruta_pop = frutas.pop() #removeu o ultimo elemento
print(frutas) 
print(fruta_pop) #imprime o elemento removido


#zip
""" 
Agrupa os elementos correspondentes de duas (ou mais) listas.

Para no tamanho da menor lista:
só combina até onde todas as listas ainda têm elementos. Se uma das listas for mais curta, ela "corta" as outras no mesmo ponto.
exemplo:
nomes = ['Ana', 'Beto', 'Carlos']
idades = [20, 25]  # só 2 elementos!

for nome, idade in zip(nomes, idades):
    print(nome, idade)
nesse caso aqui, só retona ana 20 e beto 25, sem o carlos, pq nao tem idade pra ele

Retorna um iterador, que você pode converter em list() se quiser ver o resultado direto:
Quando você faz zip(lista1, lista2), o resultado não é uma lista comum, 
mas um iterador — um tipo de objeto que fornece os dados sob demanda, um por vez.
O resultado de zip() não é uma lista, mas sim um iterador. Para visualizar o conteúdo, converta com list() ou tuple()
Ele só pode ser percorrido uma vez (como uma torneira: depois que a água passa, acabou).
exemplo:
z = zip([1, 2, 3], ['a', 'b', 'c'])
print(z)            # <zip object at 0x...> (não mostra conteúdo)
print(list(z))      # [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(z))      # []  ← já foi consumido!

se quiser reutilizar:
pares = list(zip([1, 2], ['x', 'y']))
(tem que transformar em lista)
"""
nomes = ['Ana', 'Beto', 'Carlos']
idades = [20, 25, 30]

combinado = zip(nomes, idades)

for nome, idade in combinado:
    print(f"{nome} tem {idade} anos")

#outro
pares = [('a', 1), ('b', 2), ('c', 3)]
letras, numeros = zip(*pares) # desempacotar elementos de uma lista (ou outro iterável) e passá-los como argumentos separados para uma função0
print(letras)   # ('a', 'b', 'c')
print(numeros)  # (1, 2, 3)

#set

""" 
É um conjunto não ordenado, sem elementos repetidos

Usa chaves: {} ou set()

Pode ser modificado (é mutável)

Muito útil para operações como união, interseção, diferença

"""
numeros = [1, 2, 2, 3, 4, 4]
sem_repetidos = set(numeros)
print(sem_repetidos)  # {1, 2, 3, 4}

#outro

s = {1, 2, 3}
s.add(4)
s.remove(2)
print(s)  # {1, 3, 4}

#para verificar se há intersenção entre os grupos
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # {3}


#frozenset
"""
É uma versão imutável do set

Depois de criado, não pode ser alterado

Também não tem ordem, nem elementos repetidos

Útil quando você precisa de um conjunto imutável, por exemplo, como chave de dicionário
"""


#união, intersenção e diferença

""" 
funciona com SET e FROZENSET
"""
A = {1, 2, 3}
B = {3, 4, 5}

#uniao: junta todos os elementos, sem repetição

print(A | B)           # {1, 2, 3, 4, 5}
#ou
print(A.union(B))

#interseção: elementos comuns
print(A & B)           # {3}
print(A.intersection(B))

#diferenca: o que tem em A e não tem em B
print(A - B)           # {1, 2}
print(A.difference(B))

#range pode ser convertida em listas/tuplas

for i in range(3):
    print(i)  # 0 1 2

print(list(range(1, 6)))  # [1, 2, 3, 4, 5]
print(tuple(range(0, 10, 2)))  # (0, 2, 4, 6, 8)
