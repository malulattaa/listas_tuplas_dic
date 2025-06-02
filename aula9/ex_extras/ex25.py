#Dado uma lista de nomes, retorne quantos nomes têm mais de 6 letras e começam com a letra B

def comeca_com_b(nome):
    b = [x for x in nome if x[0].lower() == 'b' ]
    return b

def mais_de_6_letras(nome):
    letras = [x for x in comeca_com_b(nome) if len(x) > 6]
    return letras

def contar_nomes(lista):
    contar = len([x for x in mais_de_6_letras(lista)])
    return contar

print(contar_nomes(['Beatriz', 'Bruna', 'Carlos', 'Benedito', 'Ana']))