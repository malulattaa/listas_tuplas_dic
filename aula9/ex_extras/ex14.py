def media_multiplos_3(lista):
    resultado = sum([x for x in lista if x % 3 == 0]) / len([x for x in lista if x % 3 == 0]) if any(x % 3 == 0 for x in lista) else 0
    """ 
    multiplos = [x for x in lista if x % 3 == 0]
if multiplos:
    resultado = sum(multiplos) / len(multiplos)
else:
    resultado = 0
    """
    return resultado 

print(media_multiplos_3([3, 4, 6, 8, 9]))
"""Objetivo: Somar os múltiplos de 3 e retornar a média."""