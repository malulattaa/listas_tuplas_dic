numeros = [1,1,2,6,9,8,5,5,36,3,3,4,5,1,10]

valor = int(input("Qual número deseja ver a quantidade de vezes que ele aparece? "))

def qtde(numeros):
    quantidade = numeros.count(valor)
    return quantidade

print(qtde(numeros))