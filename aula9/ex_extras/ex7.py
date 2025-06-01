def buscar_par(lista):
    for numero in lista:
        if numero % 2 == 0:
            #6
            return numero
    return None

print(buscar_par([1, 3, 5, 6, 7]))

