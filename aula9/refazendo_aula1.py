def func1(x, y):
    h = [x ** 2 for x in func2(y)]
    #fazer do jeito da logica com map
    #h = x ** func2(y)
    #h = [2** x for x in func2(y)] seguindo a logica que tava, pra mim tinha que ficar assim
    return h
#2 elevado 3 = 8
#func2(3)
#x = 2, y = 3
#8, 64, 
def func2(x): #func2(3)
    u = [i ** 0.5 for i in func3(x, x * 2, x *3)]
    return u 
    #3, 6, 9 
    # 3, 6, 9

def func3(a, b, c):
    lista = [x**2 for x in [a,b,c] if x % 3 == 0]
    return lista
#a = 3 - 9
#b = 6 - 36
#c = 9 - 81

print(func1(2, 3))

