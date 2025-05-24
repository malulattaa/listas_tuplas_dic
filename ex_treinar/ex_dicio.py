""" 
Crie um dicionário com 3 frutas e seus respectivos preços.
"""

frutas = {}


i = 0
while i<3:
    fruta = input("Digite uma fruta: ")
    valor = int(input("Digite o valor dessa fruta: "))
    frutas[fruta] = valor
    i+=1

print(frutas)

add = input("Deseja adicionar nova fruta? ").lower()
if add == "sim":
    fruta = input("Digite uma fruta: ")
    valor = int(input("Digite o valor dessa fruta: "))
    frutas[fruta] = valor
    print(frutas)
else:
    print(frutas)
    
frutas["banana"] = 2
print(frutas)

remover = input("Deseja remover alguma fruta? ").lower()

if remover == "sim":
    chave = input("Qual fruta deseja remover? ")
    if chave in frutas:
        frutas.pop(chave)
        print("fruta removida!")
        print(frutas)
    else:
        print("Essa fruta não consta!")
        
