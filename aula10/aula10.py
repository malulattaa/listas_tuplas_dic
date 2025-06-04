import math
import random
""" 
lambda function

funções anonimas/indefinidas

como era:
def nome(x, y, z):
    corpo da func

sintaxe: 
lambda argumentos: exmpressão


argumentos poderiam ser no caso (x, y, z), em lambda nao precisa de ()
expressão: corpo da função
    sao funcoes expressas, algo mt pontual (nada de 4/5 linhas, se for assim cria uma função de vdd)
"""

dobro = lambda x: x * 2
#sozinha é igual uma lista sozinha = nao serve pra mt coisa
#deve ser combinada 

print('exemplo  - 1 Dobro de 5: ', dobro(5))

soma = lambda x, y: x + y
#nao precisa de return, sempre vai retornar o valor
print('Exemplo - 2 Soma de 3 e 4: ', soma(3, 4))

hipotenusa = lambda ca, co: ((ca ** 2) + (co ** 2))**0.5
print('Exemplo - 3: Hipotenusa: ', hipotenusa(6,8))

hipo = lambda a,b: math.sqrt(a**2 + b**2)
print('Exemplo - 3: Hipotenusa: ', hipo(6,8))

#filter, map
#filter vai aplicar uma função em cada um dos elementos de um iteravel e vai retornar
#aquele que for True, o que for False n passa e n retorna
#map aplica uma função em cada elemento de um iteravel e vai tranforma-los, devolver um 
#array ?????

numeros = [1,2,3,4,5,6,7,8,9,10]

#filter sempre precisa de uma função de verificação

#parametros da funcao filter: filter(func, array)
#func precisa retornar True ou False
pares = list(filter(lambda x: x % 2 == 0, numeros))
pares = list(filter(lambda x: x % 2 == 0, list(map(lambda x: x**2, numeros))))
#pares = list(filter(lambda x: x % 2 == 0, list(map(lambda x: x**2, list(filter)))))
                                                                    #continuar com map
print('Exemplo - 4: Números pares: ', pares)

""" 
gere 100 num randomicos de 20 a 100, filtre > 60
gere 100 num randomicos de 20 a 100, filtre > media
gere 100 num randomicos de 20 a 100, filtre < 25
"""
lista = [random.randint(20,100) for x in range(100)] 
print(lista)

num = list(filter(lambda x: x > 60, lista))
print('Exemplo - 4: Números maiores que 60 ', num)

menor = list(filter(lambda x: x < 25, lista))
print('Exemplo - 4: Números menores que 25 : ', menor)

media = list(filter(lambda x: x > sum(lista) / len(lista), lista))
print('Exemplo - 5: Média: ', media)

#map
#list(map(func, array))
#filter = filtragem
#trandormações = map
    #o intuito n é tirar itens da lista original

quadrado = list(map(lambda x: x**2, numeros))

#sorted(pessoas, key = lambda x: x[1])
pessoas = [("Ana", 19), ('João', 30), ("Maria", 20)]


crescente = list(reversed(sorted(pessoas, key = lambda x: x[1])))
print(crescente)
