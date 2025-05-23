""" 
Dadaumalista de nomes, retorne uma nova lista com os nomes em letras mai´ usculas
"""

#fazer um len pra passar nas letra e por um lower na primeira
lista_nome = []

while True:
    nome = input("Digite nomes para adicionar na lista ou (sair) para encerrar a execução: ").lower()
    if nome == "sair":
        break
    lista_nome.append(nome)

for i in lista_nome:
    maiuscula = i.capitalize()
    print(maiuscula)

#sem o capitalize

for i in lista_nome:
    m = i[0].upper() + i[1:].lower() #1: pega o restante
    print(m)
    
#acho que não precisaria do for aq