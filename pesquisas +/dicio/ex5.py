pessoas = {}
lista_pessoas = []
while True:
    pessoas['nome'] = input("Nome: ")
    while True:
        pessoas['sexo'] = input("Sexo (F/M): ").upper()
        if pessoas['sexo'] in 'MF':
            break
        print("Erro")
    pessoas['idade'] = int(input("Idade: "))
    lista_pessoas.append(pessoas.copy())
    while True:
        sair = input("Deseja continuar cadastrando [S/N]? ").upper()
        if sair in 'SN':
            break
        print("Erro")
    if sair == 'N':
        break


#quantas pessoas foram cadastradas

qtde = len(lista_pessoas)
print(f"O número total de pessoas cadastradas foi igual a {qtde} ")

media = sum(i['idade'] for i in lista_pessoas) / len(lista_pessoas)
print(media)

mulheres = [m['nome'] for m in lista_pessoas if m['sexo'] == 'F']
print(mulheres)

acima_media = [a['nome'] for a in lista_pessoas if a['idade'] > media]
print(acima_media)