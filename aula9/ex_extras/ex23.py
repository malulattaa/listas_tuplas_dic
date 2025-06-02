""" 
Crie duas funções:

quadrado(x) → retorna o quadrado de um número

processar(lista) → usa a função quadrado e retorna uma nova lista com o quadrado dos números pares da lista original.

"""

def quadrado(x):
    quadrado = [x**2 for x in processar(x)]
    return quadrado

def processar(lista):
    par = [x for x in lista if x % 2 == 0 ]
    return par
    
print(quadrado(processar([1, 2, 3, 4])))