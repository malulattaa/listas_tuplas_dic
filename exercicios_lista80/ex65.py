"""Fa¸ca um programa que recebe nomes de alunos e suas idades. Armazene usando
uma lista de tuplas e depois transforme em dicion´ario."""

lista = []
while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    lista.append((nome, idade))
    
    while True:
        add = input("Deseja continuar adicionando? (S/N) ").upper()
        if add in "SN":
            break
        print("Digite S ou N")
    if add == "N":
        break
    
dicionario = dict(lista)

for c, v in dicionario.items():
    print(f"{c} : {v}")