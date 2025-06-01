def gerar_multiplos(n):
    return [n * i for i in range(1, 4)]
""" 
3*1 = 3
3*2 = 6
3*3 = 9
"""

def elevar(lista):
    return [x ** 2 for x in lista if x % 2 != 0]
#9, 36, 81
# impar: 9, 81

def resultado(n):
    return elevar(gerar_multiplos(n))

print(resultado(3))
