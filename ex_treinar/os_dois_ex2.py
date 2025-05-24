"""
Dado um dicionário com alunos e suas listas de notas, crie um novo dicionário que contenha o nome e a média de cada aluno.
"""

dicio = {
    "Ana": [8, 9, 10],
    "Beto": [5, 6, 7],
    "Carla": [9, 8, 10]
}

dados = {}

for nome, notas in dicio.items():
    media = sum(notas) / len(notas)
    
    dados[nome] = media 
print(dados)
"""


soma = [sum(notas) for notas in dicio.values()]
qtde = len(dicio.values())
print(soma)
print(qtde)

media = [i/qtde for i in soma]
print(media)

nome = len(dicio.keys())
dados[nome] = len(media)

for nome, media in dados.items():
    print(f"Nome: {nome}, média: {media}")"""