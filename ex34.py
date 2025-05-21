"""
Fa¸ca um programa que leia n´ umeros do usu´ ario at´ e digitar-1. Depois, imprima a
m´ edia
"""
numeros = []
qtde = []
while True:
    n = int(input("Digite um número ou digite -1 para sair: "))
    if n == -1:
        break
    numeros.append(n)
    
qtde = len(numeros)

def somar(*args):
    return sum(args)
media = somar(*numeros) / qtde
print(media)