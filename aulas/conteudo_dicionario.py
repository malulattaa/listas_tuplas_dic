import random
""" 
dicionarios 

definição: uma lista de associações compostas por UMA CHAVE "UNICA"
    um dicionario nao pode existir com duas chaves iguais
    SAO MUTAVEIS (os dados, as chaves podem mas nao costumam)
        a chave precisa ser de qualquer tipo e mutavel
    dicionarios nao garantem que estejam ordenados
    um elemento relacionado a outro, ou um objeto relacionado ao outro 
    
sintaxe:
dict = {"a": 1, "b": 2, "c": 3}
o primeiro é uma chave: identifica o dado
o segundo é valor
    o valor pode ser uma lista
    dict = {"a":( 1, 2, [1, 2, {1:20, 2:30}]), "b":20)
    
    dicionario e lista nao pode ser chave
    tupla pode mas nao é muito usual 
        d = {
        (1, 2): "coordenadas",
        ("a", "b"): "letras"
    }
    print(d[(1, 2)])  # saída: coordenadas

"""
"""
dic = {"nome1": "beto", "nome2": "ana", "nome3": "victor"}

dic["nota"] = 7.80

# o print só é usado nesse caso para debug
print(dic)

#dic = {(1, 2, 3): "beto"} pode

itens = dic.items()
chaves = dic.keys()
valores = dic.values()

print(f"itens = {itens}")
print(f"chaves = {chaves}")
print(f"valores = {valores}")

#retorna uma lista de tuplas

for i, j in dic.items():
    print(f"i = {i} e j = {j}")
print("")
for i in dic.keys():
    print(f"chaves = {i}")
print("")
for i in dic.values():
    print(f"valores = {i}")
"""

""" 
leiam o nome de 5 pessoas e armazene em um dicionario

"""


"""
nomes = {}
for i in range(5):
    nome = input("Digite um nome: ")
    nomes[i] = nome
print(nomes)""

"""
#gerar um dic com 20 numeros inteiros e somar eles

num = {}

for i in range(20):
    num[i]=random.randint(1,20)

soma = sum(num.values())
print(soma)

#outro jeito: fazer outro for j  e fazer uma função

#outro

num = {}
soma = 0
for i in range(20):
    num[i]=random.randint(1,20)
    soma += num.get(i)
print(soma)
#get busca um elemento dentro de um dicionario pela chave 
    #print(dic.get("nome1"))

#Compreensão de listas

lista = [i for i in range(5)] # [0, 1,2,3,4]
print(lista)

lista = [i**2 for i in range(5)] 
print(lista)

#dar uma olhada qnd é com numeros decimais

for i in [0.2,0.3,0.4,0.5]:
    pass


#PESQUISA
#como trabalhar com compreensão de listas
    #lista2 = [x, y for in range(3) if x>10]
    #lista2 = [x, y for in range(3) for y in range(6) if x == y: x+=2]

'''
ex 3 - crie um programa para ler o nome, a matricula e as 4 notas de 5 alunos e armazene em um dicionario
notas podem ser geradas de forma aleatoria com o uso de compreensao de listas

saida: 
{matricula: {nome, notas:[n1,n2.n3,n4]}}


a) mostrar o aluno com a maior media 
b) % de alunos com media maior que 8
c) % de alunos reprovados considerando media de reprovação < 4
'''

dados = {}
notas = []
for j in range(1,6):
    nota = random.randint(1,10)
    notas.append(nota)
    
for i in range(2):
    nome = input("Digite um nome: ")
    matricula = int(input("Digite o número da matrícula: "))
    dados[i] = matricula,nome,notas

print(dados)

#for items in dados.items():
#dados = {matricula: {nome, notas}}