""" 
Dada uma lista de palavras, junte todas elas em uma string separada por v´ ırgulas
"""

palavras = ['palavras', 'sei la', 'alguma coisa', 'juroo']

"""for i in range(len(palavras)):
    print(palavras[i], end =', ')"""
    
junto = ", ".join(palavras)
print(junto)

""" 
.join() em Python serve para juntar (ou concatenar) os elementos de uma lista (ou de qualquer iterável de strings) 
em uma única string, usando um separador que você escolher.

'SEPARADOR'.join(lista)

"""