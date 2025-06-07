dicio = {}
lista = []
from datetime import datetime

dicio['nome'] = input("Nome: ")
ano_nasc = int(input("Digite o ano de nascimento: "))
dicio['idade'] = (datetime.now().year - ano_nasc)
dicio['CTPS'] = int(input("Número da carteira de trabalho (digite 0 se não tiver): "))
if dicio['CTPS'] != 0:
    dicio['ano_contrat'] = int(input("Qual o ano da contratação? "))
    dicio['salario'] = int(input('Salário: '))
    aposentadoria = (dicio['idade'] + (dicio['ano_contrat'] + 35) - datetime.now().year)
    dicio['aposentadoria'] = aposentadoria
else:
    print(f"{dicio['nome']} tem {dicio['idade']} anos e não possui carteira de trabalho")
lista.append(dicio.copy())
for x in lista:
    for c, v in x.items():
        print(f"o {c} tem o valor {v}")


#35 - idade