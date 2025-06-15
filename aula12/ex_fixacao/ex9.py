""" 
Imprimir uma string ao contrário, caractere por caractere
"""

def contrario(string):
    if len(string) <= 0:
        return string
    print(string[-1], (""))
    contrario(string[:-1])

(contrario("maria"))
