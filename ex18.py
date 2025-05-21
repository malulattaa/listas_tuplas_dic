""" 
Verifique se o n´ umero 7 est´a presente na lista [3, 6, 9, 12]
"""

lista = [3, 6, 9, 12]

for i in range(len(lista)):
    if lista[i] == 7:
        tem = True
    else:
        tem = False

if tem == True:
    print("Tem 7")
else:
    print("Não tem 7")
    
