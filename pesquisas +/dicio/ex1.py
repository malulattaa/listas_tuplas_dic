"""faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No
final, mostre o conteúdp da estrtura na tela"""

dicio = {}

dicio['nome'] = input("Digite o nome do aluno: ")
dicio['media'] = int(input("Digite a média: "))

if 0 < dicio['media'] < 6:
    dicio['situacao'] = 'reprovado'
elif dicio['media'] > 10 or dicio['media'] < 0:
    dicio['situacao'] = 'média inválida'
else:
    dicio['situacao'] = 'aprovado!'

print(f"O aluno {dicio['nome']} tem média {dicio['media']} e está {dicio['situacao']}")