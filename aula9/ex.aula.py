
def func1(x, y):
    h = [x ** 2 for x in func2(y)]
    return h
    # x**3

def func2(x):
    r = []
    for i in func3(x, x * 2, x *3):
        r.append(i**0.5)
    return r
    #3, 3**2, 3 **3 e depois a raiz da lista

def func3(a, b, c):
    lista = [x**2 for x in [a,b,c] if x % 3 == 0]
    #mudando pra 3
    return lista

print(func1(2, 3))

#ter cuidado com o que retorna