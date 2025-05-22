"""  Implemente um sistema que simule um carrinho de compras: adi¸c˜ ao, remo¸ c˜ao e
total de itens com pre¸cos

Preciso considerar: 
- nome do produto
- quantidade
- valor

fazer um lista de produtos com seus preços e pedir pro usuario escolher o produtos

TENHO QUE PERGUNTAR SE ELE DESEJA CONTINUAR COMPRANDO DEPOIS DE ADD CADA UM E TENHO QUE PERGUNTAR ANTES DE TUDO SE ELE QUER ADICIONAR OU REMOVER MEU DEUS ME AJUDA
"""

print("Seja bem vindo! Selecione os produtos que deseja adicionar em seu carrinho. A seguir, a tabela com os produtos e seus respectivos preços, não esqueça de selecionar corretamente e digitar a quantidade desejada. Boas compras!")
print("")
print("Produto 1 - Camiseta (50,00)")
print("Produto 2 - Calça (70,00)")
print("Produto 3 - Tênis (110,00)")
print("Produto 4 - Bolsa (30,00)")
carrinho = []

def mult(preco, qtde):
    total = preco * qtde
    return total


while True:
    produto = int(input("Digite o número do produto que deseja: "))
    qtde = int(input("Digite a quantidade: "))
    if produto == 1:
        carrinho.append({'produto': 'Camiseta', 'preco': 50, 'qtde': qtde})
        total = mult(50, qtde)
        print(f"Carrinho: {carrinho}")
        print(total)
    elif produto == 2:
        carrinho.append({'produto': 'Calça', 'preco': 70, 'qtde': qtde})
        total = mult(70, qtde)
        print(f"Carrinho: {carrinho}")
        print(total)
    elif produto == 3:
        carrinho.append({'produto': 'Tênis', 'preco': 110, 'qtde': qtde})
        total = mult(110, qtde)
        print(f"Carrinho: {carrinho}")
        print(total)
    elif produto == 4:
        carrinho.append({'produto': 'Bolsa', 'preco': 30, 'qtde': qtde})
        total = mult(30, qtde)
        print(f"Carrinho: {carrinho}")
        print(total)
    else:
        