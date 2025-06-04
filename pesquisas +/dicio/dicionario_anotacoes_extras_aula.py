import random
""" 

A chave tem que ser de um tipo imutável, como str, int, float, ou tuple.
Não pode usar listas ou dicionários como chave, porque são mutáveis.
Dicionários guardam dados no formato chave:valor, e cada chave deve ser única.
Você pode alterar, adicionar ou remover itens no dicionário.





"""

#Adicionando a chave "nota" ao dicionário.
dic = {"nome1": "beto", "nome2": "ana", "nome3": "victor"}
dic["nota"] = 7.80


# Métodos úteis:
dic.items()     # retorna pares (chave, valor)
dic.keys()      # retorna apenas as chaves
dic.values()    # retorna apenas os valores


#Itera sobre o dicionário, mostrando chave = i e valor = j.
for i, j in dic.items():
    print(f"i = {i} e j = {j}")


#Cria um dicionário onde a chave é o número da vez (0 a 4) e o valor é o nome digitado.
nomes = {}
for i in range(5):
    nome = input("Digite um nome: ")
    nomes[i] = nome
    #dicionario[chave] = valor
""" 
Quando você escreve nomes[i] = nome, o Python está:
-Verificando se a chave i já existe no dicionário:
-Se não existir, ele cria essa chave com o valor.
-Se já existir, ele atualiza o valor.
"""
print(nomes)

#Cria um dicionário com 20 números aleatórios e soma os valores com sum().
num = {}
for i in range(20):
    num[i] = random.randint(1, 20)
soma = sum(num.values())

#outro

#Usa .get(chave) para buscar o valor de cada chave, e acumula a soma.
soma = 0
for i in range(20):
    num[i] = random.randint(1, 20)
    soma += num.get(i)
#O método .get(chave) é usado para acessar o valor de uma chave no dicionário, como se fosse:
#num[i]
#poderia usar: soma += num[i]
#geralmente se usa .get() quando não tem certeza se a chave existe.

#há um problema em colocar random como chave pois pode gerar uma chave que ja existe, por ser aleatoria
#pode fazer com um while

num = {}
while len(num) < 10: #ate o dicionario atingir 9
    chave = random.randint(0, 20) #gera chave aleatoria de 0 a 20
    if chave not in num: #se a chave n existir no dicionario
        num[chave] = len(num) #add

print(num)


#ADICIONANDO ELEMENTOS A UM DIC

dados = {}

chave = input("Digite o nome da chave que deseja adicionar: ")
valor = input("Digite o valor para essa chave: ")

dados[chave] = valor

print("Dicionário atualizado:", dados)


#ALTERAR

dados = {"nome": "Maria", "idade": "18"}

chave = input("Qual chave você deseja alterar? ")

if chave in dados:
    novo_valor = input(f"Digite o novo valor para '{chave}': ")
    dados[chave] = novo_valor
    print("Valor alterado com sucesso:", dados)
else:
    print("Essa chave não existe no dicionário.")


#REMOVER

dados = {"nome": "Maria", "idade": "18", "curso": "ADS"}

chave = input("Qual chave você deseja remover? ")

if chave in dados:
    dados.pop(chave)
    print(f"Chave '{chave}' removida com sucesso.")
else:
    print("Essa chave não existe no dicionário.")

print("Dicionário agora:", dados)

"""REMOVER TUDO

aluno.clear()
print(aluno)  # {}
"""