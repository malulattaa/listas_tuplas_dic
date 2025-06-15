""" 
Recursividade é uma técnica de programação onde a função 'chama a si mesma' para resolver algum problmea

Características principais:
1. Caso base: condição de parada que evita chamadas infinitas
2. Caso recursivo: onde a função 'chama a si mesma' com um propósito menor
    #td vez que chama precisa aumentar ou diminuir o valor
"""

def func(x):
#nao se utiliza break para sair de func recursiva
#caso base
    if x<1:
        return 0
    return x + func(x - 1)

# 3 + func(2)
# 3 + func(1)
# 3 + func(0)
    
print(func(10))

def funcao(x):
    if x<=1:
        return 1
    funcao(x-1)
    return x * funcao(x - 1)
#estudar do pq nao retorna o valor da multiplicação e sim o valor de x-1
print(funcao(5))

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n - 2)
    #modificar aq pra imprimir a sequencia 
print(fibonacci(7))
""" 
ex 1 - Inverter string: crie uma função recursiva q inverta uma string
"""
def inverter(string):
    if len(string) <= 1:
        return string[0]
    return string[-1] + inverter(string[:-1])

print(inverter("farmacia"))

"""
ex 2 - Potência: implemente uma função recursiva que calcule a^b, onde a e b são números inteiros e b>=0
"""

#a*a n -1
def elevar(a, b):
    if b <= 0:
        return 1
    return a * elevar(a,b- 1)

print(elevar(5, 2))