import random

""" 
Crie uma lista com 5 n´ umeros e calcule a m´edia usando la¸co for
"""

numeros = []

for i in range(5):
    add = random.randint(0, 10)
    numeros.append(add)
print(numeros)

soma = sum(numeros)
for j in range(len(numeros)+1):
    qtde = j
    
media = soma / qtde
print(f"A média foi: {media}")
    
    
    
    