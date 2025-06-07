#lambda recebe um valor: oq ela deve dar como resposta
#ex.

calcular_imposto = lambda x: x * 0.3

print(calcular_imposto(1000))

precos = [180, 500, 10, 25]

#impostos= list(map())
#vantagem do lambda: funcao como parametro para outra função
#map pega uma lista de info e aplica sobre cada um desses valores, uma função
#mult por 2, map pega todos os valores da lista e multiplica cada um por 2
#map precisa da funcao que vc vai alicar e a lista de informações
#a função dentro de map pode ser um função normal, ou pode ser feita uma função lambda dentro dela
#ex.

#declarei essa função para usar ela no map da lista precos
def calcular_imposto(preco):
    return preco * 0.3

print(calcular_imposto(1000))

#entao ficaria assim:
imposto = list(map(calcular_imposto, precos))
print(imposto)

#ou na função, fazer um lambda direto:
impostos = list(map(lambda x: x*0.3, precos))
print(impostos)

#se nao por o list, ele retorna como objeto na memoria