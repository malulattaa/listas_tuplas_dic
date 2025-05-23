""" 
Solicite nomes at´e que o usu´ ario digite ”sair”. Armazene em uma lista e imprima
"""
nomes = []
while True:
    nome = input("Digite um nome ou (sair) para encerrar: ")
    nomes.append(nome)
    if nome == 'sair':
        break

nomes.pop(-1)
print(nomes)


