""" 
Crie uma função que receba uma lista de nomes e retorne apenas os que possuem mais de 5 letras.

"""
def cinco_letras(lista):
    entrada = [x for x in lista if len(x) > 5]
    return entrada


print(cinco_letras(['Ana', 'Gabriel', 'Lucas', 'Beatriz']))

