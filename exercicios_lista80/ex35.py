""" 
Crie uma lista de tuplas contendo nomes e idades. Imprima os nomes das pessoas
com mais de 18 anos.
"""

lista = []

while True:
    nome = input("Digite seu nome: ").lower()
    if nome == 'sair':
        break
    idade = int(input("Digite sua idade: "))
    tupla = (nome, idade)
    lista.append(tupla)

for nome, idade in lista:
    if idade >18:
        print(f"{nome} tem {idade} anos")