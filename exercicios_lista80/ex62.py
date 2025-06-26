""" 
Crie uma lista de dicion´arios com nome, idade e cidade. Imprima os dados de cada
pessoa
"""


lista = []
while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")
    
    pessoa = {
        'nome' : nome,
        'idade' : idade,
        'cidade' : cidade,
    }
    lista.append(pessoa)
    
    while True:
        continuar = input("Deseja continuar? (S/N)").upper()
        if continuar in "SN":
            break
        print("Erro")
    if continuar == 'N':
        break

print(lista)
for p in lista:
    for c, v in p.items():
        print(f"{c} : {v}")
    print("")