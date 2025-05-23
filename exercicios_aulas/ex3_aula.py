import random

'''
ex 3 - crie um programa para ler o nome, a matricula e as 4 notas de 5 alunos e armazene em um dicionario
notas podem ser geradas de forma aleatoria com o uso de compreensao de listas

saida: 
{matricula: {nome, notas:[n1,n2.n3,n4]}}


a) mostrar o aluno com a maior media 
b) % de alunos com media maior que 8
c) % de alunos reprovados considerando media de reprovação < 4
'''
media_lista =[]
medias = {}
dados = {}
for i in range(1,6):
    matricula = random.randint(100,999)
    nome = input("Digite um nome: ")
    
    notas = [random.randint(0,10) for j in range(4)]
    media = sum(notas) / len(notas)
    media_lista.append(media)
    maior_media = max(media_lista)
    print(maior_media)
    medias[nome] = media  #descorbrir como fazer pra imprimir o nome respectivo a maior media
    print(medias)
    
        
    dados[matricula] = {nome:notas}
    
for matricula, nome_nota in dados.items():
    for nome, notas in nome_nota.items():
        print(f"{matricula} : {nome} - Notas: {notas}")



#dicionario que usa tupla como chave e a chave é um coldigo binario pra decodificar
#for items in dados.items():
#dados = {matricula: {nome, notas}}