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
