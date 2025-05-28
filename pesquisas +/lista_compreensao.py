""" 
É uma forma rápida e prática de criar listas em Python, usando uma sintaxe compacta

ESTRUTURA:
[nova_expressao for item in iterável if condição]

nova_expressao: o que você quer adicionar à lista

item: cada elemento do iterável (exemplo: uma lista, range, etc)

condição (opcional): filtra quais elementos serão incluídos

ex:
quadrados = [i ** 2 for i in range(1, 6)]
print(quadrados)
# Saída: [1, 4, 9, 16, 25]


ex com cond:
pares_quadrados = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(pares_quadrados)
# Saída: [4, 16, 36, 64, 100]

"""

lista = [i for i in range(5)] 
# Resultado: [0, 1, 2, 3, 4]


lista = [i**2 for i in range(5)] 
# Resultado: [0, 1, 4, 9, 16]


#A sintaxe correta de listas de compreensão com dois for:
    #lista = [resultado for x in range(...) for y in range(...) if condicao]



#quando tem dois for dentro da lista, o segundo for significa que esta dentro do primeiro, por isso cada valor do segundo precisa passar por cada valor do primeiro
#ex:

produto_cartesiano = [(x, y) for x in range(3) for y in range(2)]
print(produto_cartesiano)  # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
"""
| x | y | tupla gerada |
| - | - | ------------ |
| 0 | 0 | (0, 0)       |
| 0 | 1 | (0, 1)       |
| 1 | 0 | (1, 0)       |
| 1 | 1 | (1, 1)       |
| 2 | 0 | (2, 0)       |
| 2 | 1 | (2, 1)       |
"""

tabelas = [[i * j for j in range(1, 6)] for i in range(1, 4)]
print(tabelas)
#Para cada i de 1 a 3 (inclusive), ele cria uma lista com os produtos i * j, onde j vai de 1 a 5.
""" 
Para i = 1:
[1*1, 1*2, 1*3, 1*4, 1*5] → [1, 2, 3, 4, 5]

Para i = 2:
[2*1, 2*2, 2*3, 2*4, 2*5] → [2, 4, 6, 8, 10]

Para i = 3:
[3*1, 3*2, 3*3, 3*4, 3*5] → [3, 6, 9, 12, 15]

"""

#dicio

dicio = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


#conjunto: maneira de usar set (nao repete)
conjunto = {x % 3 for x in range(10)}
print(conjunto)


#gerador: gera um valor por vez
#sintexe:
#gerador = (expressão for variável in iterável)
gerador = (x**2 for x in range(5))
#só printar isso aq n funciona, tem que percorrer ele 
for valor in gerador:
    print(valor)


string = [ i for i in "programe em python"]
print(string) #retorna cada letra 

string = [ i for i in "programe em python" if  i in "aeiou"]
print(string) #retorna as vogais

string = [ i for i in ["programe", "python", "algo sem p"] if  i.startswith('p')]
print(string) #só retona as que começam com p

#lista de listas

lista_de_listas = [["programe", "a"], ["python","b"], ["teste" , "c"]]

sublista = [i[0] for i in lista_de_listas]
#para cada item dessa lista (cada lista), ele pega o primeiro elemento
print(sublista)

#para pegar o segundo elemento
sublista = [i[1] for i in lista_de_listas]
print(sublista)

#todos os elementos 

sublista = [item for lista in lista_de_listas for item in lista]
print(sublista)
#item cria uma nova lista com cada item encontrado
# for lista in lista_de_listas esta percorrendo cada sublista dentro da lista principal.
# for item in lista: Para cada lista (sublista), ele percorre cada item.

#para dicio 

dicio = {"programe": "a", "python":"b", "teste" : "c"}

percorrendo = [i for i in dicio]
print(percorrendo) #percorre chaves

percorrendo = [i for i in dicio.values()]
print(percorrendo) #percorre valores


#dobrar valor de produtos

listas_preco = [1000, 1500, 2000, 600, 100]

nova_lista = [preco * 2 for preco in listas_preco]
print(nova_lista)

#produtos que custarem acima de 1000 dol, importo de 50% sobre o valor total

#fazendo com o for normal

imposto = []
for preco in listas_preco:
    if preco > 1000:
        imposto.append(preco*0.5)
print(imposto)

comp = [preco*0.5 for preco in listas_preco if preco > 1000]
print(comp)