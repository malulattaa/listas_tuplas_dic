""" 
Implemente um sistema de cadastro de usu´arios com login, utilizando listas de
tuplas.
"""
usuarios = []
def cadastrar():
    while True:
        print("Cadastro: ")
        email = input("Digite o e-mail para cadastrar: ")
        senha = int(input("Senha: (apenas números) "))
        usuarios.append((email, senha))
        print("")
        while True: 
            add = input("Deseja continuar adicionando? ").upper()
            if add in "SN":
                break
            print("S ou N")
        if add == 'N':
            break

    while True:
        print("Logar")
        valid_email = input("Digite o email para logar: ")
        valid_senha = int(input("Senha para logar: "))
        if (valid_email, valid_senha) in usuarios:
            print("Logado com sucesso!")
            break
        else: 
            print("Dados incorretos. Tente novamente")
            continue
        
cadastrar()