""" 
Dada uma lista de valores, encontre todos os pares que somam exatamente 10
"""
valores = [1, 2, 3, 7, 8, 9]
soma = [(x, y) for x in valores for y in valores if (x + y) == 10 and x<y]
print(soma)