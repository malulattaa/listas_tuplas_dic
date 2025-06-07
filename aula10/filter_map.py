#map e filter sa estrturas que o objetivo é a aplicar uma função em varios itens de uma lista

precos_produtos = {
    5000,
    9000,
    2000,
    15000,
}

def aplicar_aumento(preco):
    if preco > 6000:
        return preco * 1.1
    else:
        return preco

#no map passa a funcao sem os parenteses
#msm forma de aplicação para map e filter, só que filter retorna vdd ou falso
#filter filtra a lista de itens original
#map aplica a edição

precos_produtos = list(map(aplicar_aumento, precos_produtos))
print(precos_produtos)

def filtrar_aumento(preco):
    if preco > 6000:
        return True
    else:
        return False
filtrar_produtos = list(filter(filtrar_aumento, precos_produtos))
print(filtrar_produtos)