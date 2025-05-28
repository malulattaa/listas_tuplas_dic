"""  Implemente um sistema que simule um carrinho de compras: adi¸c˜ ao, remo¸ c˜ao e
total de itens com pre¸cos

Preciso considerar: 
- nome do produto
- quantidade
- valor

fazer um lista de produtos com seus preços e pedir pro usuario escolher o produtos

TENHO QUE PERGUNTAR SE ELE DESEJA CONTINUAR COMPRANDO DEPOIS DE ADD CADA UM E TENHO QUE PERGUNTAR ANTES DE TUDO SE ELE QUER ADICIONAR OU REMOVER MEU DEUS ME AJUDA
"""

#ARRUMAR ESSE CODIGO (REFAZER)

print("Seja bem vindo! Selecione se deseja listar os produtos do carrinho, remover ou adicionar.")
print("")
print("A - Adicionar")
print("L - Listar")
print("R - Remover")
print("")


carrinho = []

def mult(preco, qtde):
    total = preco * qtde
    return total

funcao = input("Qual operação deseja realizar? ").lower()

if funcao == 'a':
    while True:
        print("Seja bem vindo! Selecione os produtos que deseja adicionar ao seu carrinho. A seguir, a tabela com os produtos e seus respectivos preços, não esqueça de selecionar corretamente e digitar a quantidade desejada. Boas compras!")
        print("Produto 1 - Camiseta (50,00)")
        print("Produto 2 - Calça (70,00)")
        print("Produto 3 - Tênis (110,00)")
        print("Produto 4 - Bolsa (30,00)")
        print("Voltar ao menu - 5")
        print("")
        produto = int(input("Digite o número do que deseja: "))
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
            print("Esse produto não existe!")
elif funcao == 'l':
    print(carrinho)
elif funcao == 'r':
    remover = input("Qual produto deseja remover? ")
    if produto in carrinho:
        carrinho.remove(produto)
    else:
        print("O produto não está nol carrinho")
