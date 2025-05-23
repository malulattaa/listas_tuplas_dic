""" 
Implemente uma fun¸c˜ ao que receba uma lista e retorne os elementos na ordem
inversa.
"""

lista = []
inversa = []
while True:
    n = input("Digite elementos para serem impressos na ordem inversa ou (sair) para encerrar: ").lower()
    if n == 'sair':
        break
    lista.append(n)
    
for i in reversed(lista):
    inversa.append(i)
    
print(inversa)