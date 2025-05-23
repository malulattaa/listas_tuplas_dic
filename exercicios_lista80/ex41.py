a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)

lista1 = []
lista2 = []

while True:
    l1 = int(input("Digite números para a lista 1 ou digite 0 para encerrar: "))
    if l1 == 0:
        break
    lista1.append(l1)
while True:
    l2 = int(input("Digite números para a lista 2 ou digite 0 para encerrar: "))
    if l2 == 0:
        break
    lista2.append(l2)
    
intersecao = list(set(lista1) & set(lista2))
print(f"Os elementos repetidos são: {intersecao} ")
    
    

    