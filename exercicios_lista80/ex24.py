import random 
""" 
Separe uma lista de n´umeros em duas: uma com pares e outra com´ımpares
"""
numero = []
par = []
impar = []
for i in range(20):
    num = random.randint(0,100)
    numero.append(num)

for j in numero:
    if j % 2 == 0:
        par.append(j)
    else:
        impar.append(j)
        
print(f"lista de numeros pares: {par}")
print(f"lista de números ímpares: {impar}")