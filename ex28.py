""" 
Crie uma fun¸c˜ ao que receba uma lista e retorne a soma de todos os elementos
num´ ericos

"""
numeros = []
while True:
    n = int(input("Digite números para somar ou 0 para sair: "))
    numeros.append(n)
    if n == 0:
        break
    
num = tuple(numeros)
def somar(*args):
    return sum(args)
print(somar(*num))
# *:  desempacotar a tupla em múltiplos argumentos