""" 
Crie um dicion´ario que mapeia n´umeros de 1 a 5 para seus quadrados, usando la¸co
for.
"""
quadrados = {}

for n in range(1, 6):
    quadrado = n**2
    quadrados[n] = quadrado
for c, v in quadrados.items():
    print(f"{v} é o quadrado de {c}")
    
#treinando comp de dicio

quad = {n: n**2 for n in range(1,6)}
for c, v in quad.items():
    print(f"{v} é o quadrado de {c}")
    
