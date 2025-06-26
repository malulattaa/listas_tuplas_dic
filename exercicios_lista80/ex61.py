""" 
Crie um dicion´ario onde as chaves s˜ao nomes de pessoas e os valores s˜ao listas com
trˆes notas. Calcule a m´edia de cada aluno.

"""
pessoas = {}
while True:
    notas = []
    nome = input("Nome: ")
    for n in range(3):
        nota = float(input(f"Digite a {n}° nota do aluno {nome}: "))
        notas.append(nota)

    pessoas[nome] = notas
    while True:
        add = input("Deseja adicionar mais? (S/N) ").upper()
        if add in "SN":
            break
        print("S ou N")
    if add == "N":
        break
    
for c, v in pessoas.items():
    print(f"Aluno: {c}")
    print("Notas do aluno: ")
    for nota_aluno in v: 
        print(f" - {nota_aluno}")
    media = sum(v) / len(v)
    print("Média: ", media)
    print("")
