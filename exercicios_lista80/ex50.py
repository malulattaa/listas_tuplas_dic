"""Crie uma lista de tuplas com nomes e idades e retorne a pessoa mais velha e a mais
nova"""

lista = []
while True:
    nome = input("Digite o nome ou '000' para sair: ")
    if nome == '000':
        break
    idade = int(input("Digite a idade: "))
    tupla = (nome, idade)
    lista.append(tupla)

print(lista)

def conferir_idade(pessoa):
    return pessoa[1]
#sorted(pessoas, key = lambda x: x[1])
velho = max(lista, key = conferir_idade)
novo = min(lista, key = conferir_idade)

print(f"Pessoa mais velha: {velho[0]}")
print(f"Pessoa mais nova: {novo[0]}")







""" 
operator.itemgetter()
É uma função da biblioteca operator — bem eficiente para extrair um índice fixo:
from operator import itemgetter

max(lista, key=itemgetter(1))



"""