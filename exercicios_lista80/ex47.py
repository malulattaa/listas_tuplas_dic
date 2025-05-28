""" Solicite notas de alunos e armazene como tuplas (nome, nota). Ordene a lista pela
nota em ordem decrescente"""
lista = []
while True:
    print("Digite '000' para sair")
    nome = input("Digite o nome: ")
    nota = int(input("Digite uma nota: "))
    tupla = (nome, nota)
    lista.append(tupla)
    
