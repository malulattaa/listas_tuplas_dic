""" 
Crie uma lista com n´umeros de 1 a 100 e filtre os m´ultiplos de 3
"""

numeros = []
mult3 = []

for i in range(1,101):
    numeros.append(i)

for i in numeros:
    if i % 3 == 0:
        mult3.append(i)
        
print(mult3)