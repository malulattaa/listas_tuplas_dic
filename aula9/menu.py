from util import limpar_tela
from aluno import cadastrar_aluno
from professor import cadastrar_professor

def ler_opcao(lim_sup):
    #ler a opção ate que seja valido 
    op = input("Escolha a opção: ")
    if op >= 0 and op <= lim_sup:
        return op
    print("Você não digitou uma opção válida")
    return -1


def menu_principal():
    limpar_tela()
    print("+" * 20, "MENU", "+" * 20)
    print("1 - Cadastrar")
    print("2 - Matricular")
    print("3 - Consultar")
    print("4 - Relatório")
    print("0 - Sair")
    op = ler_opcao(4)
    
    #melhorar
    
    if op == 1:
        menu_cadastro()
        
def matricular():
    limpar_tela()
    print("+" * 20, "MATRICULAR", "+" * 20)
    print("1 - Alunos")
    print("0 - Voltar")
    op = ler_opcao(1)
    