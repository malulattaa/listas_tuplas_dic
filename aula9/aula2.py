
import os

alunos = []
professores = []
turmas = []

def limpar_tela():
    os.system("cls" if os.name == 'nt' else 'clear')
    
def cadastrar_aluno():
    #ler dados do aluno {cpf : 123, nome:beto, endereco : rua x, +2 campos}
    pass
    aluno = {'cpf' : '123', 'nome': 'beto', 'end': 'rua x', 'cep': '3930'}
    alunos.append(aluno)
def cadastrar_professor():
    #ler dados do aluno {cpf : 123, nome:beto, endereco : rua x, +2 campos}
    pass
    professor = {'cpf' : '123', 'nome': 'beto', 'end': 'rua x', 'cep': '3930'}
    professores.append(professor)
    
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
    
        #fazer o resto

def menu_cadastro():
    limpar_tela()
    print("+" * 20, "CADASTRAR", "+" * 20)
    print("1 - Alunos")
    print("2 - Professor")
    print("3 - Turma")
    print("4 - Voltar")
    op = ler_opcao(3)
    
    if op == 1:
        cadastrar_aluno()
    elif op == 2:
        cadastrar_professor

def matricular():
    limpar_tela()
    print("+" * 20, "MATRICULAR", "+" * 20)
    print("1 - Alunos")
    print("0 - Voltar")
    op = ler_opcao(1)
    
while True:
    menu_principal()