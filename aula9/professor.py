from datetime import datetime

professores = []
def cadastrar_professor():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    while True:
        data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
        try:
            data = datetime.strptime(data_nasc, "%d/%m/%Y").date()
            break 
        except ValueError:
            print("Data inválida. Tente novamente.")
    print("_"*10, "ENDEREÇO", "_"*10)
    rua = input("Rua: ")
    num = int(input("Número: "))
    bairro = input("Bairro: ")
    cep = input("CEP: ")
    #ler dados do aluno {cpf : 123, nome:beto, endereco : rua x, +2 campos}

    endereco = {
        'rua' : rua,
        'numero' : num,
        'bairro' : bairro,
        'cep' : cep
        
    }
    professor = {
        'nome' : nome,
        'cpf' : cpf,
        'data_nascimento' : data,
        'endereco' : endereco
        
    }
    professores.append(professor)

def listar_professores():
    if len(professores) == 0:
        print("Nenhum professor cadastrado.")
        return

    print("Professores cadastrados:")
    for prof in professores:
        print(prof['nome'])
    
    #melhorar, mostrar nome e tals
