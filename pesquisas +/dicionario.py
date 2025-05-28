""" 
Um dicionário em Python é uma coleção de pares chave: valor. 
É como uma lista, só que em vez de acessar os itens pelo índice (0, 1, 2...), você acessa pelo nome da chave.


"""

# Criando um dicionário
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia"
}

# Acessando valores
print(aluno["nome"])  # Saída: João
print(aluno["idade"]) # Saída: 20


# Adicionando um novo par chave-valor
aluno["nota"] = 8.5

# Modificando um valor
aluno["idade"] = 21

# Removendo uma chave
del aluno["curso"]

print(aluno)


filme = {
    'titulo' : 'starwars',
    'ano' : 1977,
    'diretor':'george lucas'
    
    
}
print(filme)

for k,v in filme.items():
    print(f'O {k} é {v}')
    
pessoas = {
    'nomes':'gustavo',
    'sexo' : 'M',
    'idade' : 25
    
}
print(f'O {pessoas["nomes"]} tem {pessoas["idade"]} anos')

brasil = []
estado1 = {'uf':'rio de janeiro', 'sigla' : 'rj'}
estado2 = {'uf':'são paulo', 'sigla' : 'sp'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)

estado = {}
brasil = []

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy()) #fateamento em dicio
print(brasil)

for e in brasil:
    for k,v in e.items():
        print(f"O campo {k}, Tem valor: {v}")