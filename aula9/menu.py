from util import limpar_tela
from aluno import cadastrar_aluno
from professor import cadastrar_professor
from professor import listar_professores

def ler_opcao(lim_sup):
    #ler a opção ate que seja valido 
    op = int(input("Escolha a opção: "))
    if op >= 0 and op <= lim_sup:
        return op
    print("Você não digitou uma opção válida")
    return -1


def menu_principal():
    
    print("+" * 20, "MENU", "+" * 20)
    print("1 - Cadastrar")
    print("2 - Matricular")
    print("3 - Listar")
    print("4 - Consultar")
    print("5 - Relatório")
    print("0 - Sair")
    op = ler_opcao(5)
    
    #melhorar
    
    if op == 1:
        menu_cadastro()
    elif op == 3:
        listar_professores()
        
def matricular():
    limpar_tela()
    print("+" * 20, "MATRICULAR", "+" * 20)
    print("1 - Alunos")
    print("0 - Voltar")
    op = ler_opcao(1)
    

def menu_cadastro():
    limpar_tela()
    print("+" * 20, "CADASTRAR", "+" * 20)
    print("1 - Alunos")
    print("2 - Professor")
    print("3 - Turma")
    print("4 - Voltar")
    op = ler_opcao(3)
    
    
    opcoes = {
        
        1: cadastrar_aluno,
        2: cadastrar_professor,
        #3: cadastrar_turma
        4: menu_principal
        

    }
