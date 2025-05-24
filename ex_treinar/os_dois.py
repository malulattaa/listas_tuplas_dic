""" 
Crie um dicionário onde as chaves sejam números de 1 a 5 e os valores sejam listas com os quadrados de 1 até esse número.
"""

dicio = {}



for j in range(1,6):
    chave = j
    valor = [i ** 2 for i in range(j+1)]
    dicio[chave] = valor

for a,b in dicio.items():
    print(f"{a} : {b}")
    
    
    