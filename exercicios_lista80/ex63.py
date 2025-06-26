""" 
Solicite ao usu´ario que digite pares (produto, pre¸co) e armazene em um dicion´ario.
Permita pesquisar o pre¸co por produto.

"""
estoque = {}
while True:
    produto = input("Produto: ")
    preco = float(input("Preço: "))
    
    estoque[produto] = preco
    
    while True:
        add = input("Deseja continuar adicionando? (S/N) ").upper()
        if add in "SN":
            break
        print("Digite S ou N")
    if add == "N":
        break

print(estoque)

pesquisa = float(input("Que preço deseja buscar? "))
encontrado = False
for c, v in estoque.items():
    if pesquisa == v:
        print(f"{c} : {v}")
        encontrado = True
if not encontrado:
    print("Preço não encontrado.")