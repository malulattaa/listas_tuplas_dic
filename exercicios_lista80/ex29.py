""" 
Crie um menu interativo que permita adicionar, remover, listar ou sair de um pro
grama que manipula listas
"""

lista = []

while True:
    menu = int(input("Digite 1 - adicionar / 2- remover / 3- listar ou 0 -sair: "))
    if menu == 0:
        break
    elif menu == 1:
        add = input("Que elemento deseja adicionar? ")
        if add in lista:
            print("Esse elemento já foi adicionado!")
        else:
            lista.append(add)
            print("Elemento adicionado!")
    elif menu == 2:
        remover = input("Que elemento deseja remover? ")
        if remover in lista:
            lista.remove(remover)
            print("Elemento removido!")
        else:
            print("Elemento não consta na lista, tente novamente")
    elif menu == 3:
        print(lista)
    else:
        print("Entrada inválida!")
    print("")