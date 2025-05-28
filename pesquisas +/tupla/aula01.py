"""elementos da tupla identificado por indice"""

#fateamento 

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print(lanche[2]) #pizza
print(lanche[0:2]) #hamburguer e suco (exclusivo, nao pega o 2)
print(lanche[1:])#vai do suco ate o final (começa no 1e percorre ate o final da tupla)
print(lanche[-1]) #ultimo elemento
len(lanche) #quantos elementos tem n tupla lanche
print(lanche[-1:])


    
#IMUTAVEL

    
for cont in range(0, len(lanche)):
    print(cont)
    
for c in lanche:
    print(c) #nesse caso não da pra mostrar a posição
#mesma coisa, mas um usa diretamente a variavel composta e outro usa range
for cont in range(0, len(lanche)):
    print(f"Vou comer {lanche[cont]} na posição {cont}")

#para fazer esse caso mostrar a posição 
""" for c in lanche:
    print(c)"""
for posicao, c in enumerate(lanche):
    print(f"Vou comer {c} na posição {posicao}")
    


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # a ordem aqui tem total influência
print(c)
#outra ordem
c = b + a
print(c)
print(len(c))
print(c.count(5)) #mostra quantas vezes aparece o num 5 na tupla c
print(c.index(8)) #mostra em qual posição esta o 8
#deslocamento
print(c.index(5)) # tem 5 na posicao 0 e 5, mas ele só mostra o primeiro
#se eu quiser que ele mostre alem do da posição 0, eu posso por pra ele começar a verificar o index do 5, depois da posição 1
print(c.index(5,1)) #mostra 5

pessoa = ("Gustavo", 39, "M", 99.88) #pode ter dados de tipos diferentes
del(pessoa) #apaga a tupla inteira
#por ser imutavel, nao é possivel deletar um item, apenas ela inteira


