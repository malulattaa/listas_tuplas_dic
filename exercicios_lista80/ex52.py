""" Dada uma lista de strings, ordene por ordem do n´umero de vogais em cada string """

#sorted(vogais)

vogais = ["banana", "chinelo", "bolsa", "cogumelo"]
#3, 3, 2, 4

nova_lista = sorted(vogais, key = lambda item: sum(1 for letra in item if letra in 'aeiouAEIOU'), reverse=True)
print(nova_lista)