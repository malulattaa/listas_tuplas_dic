""" 
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia. No final mostre uma listagem de preços, organizando os dados em forma tabular
"""

listagem = ("Pão" , 1, "Leite", 3.5, "Frango", 10.9)


print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
#^ centraliza 
print('_' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:>6.2f}")