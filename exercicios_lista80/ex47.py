""" Solicite notas de alunos e armazene como tuplas (nome, nota). Ordene a lista pela
nota em ordem decrescente"""
lista = []
lista_tupla = []
while True:
    print("Digite '000' para sair")
    nome = input("Digite o nome: ")
    if nome == '000':
        break
    nota = int(input("Digite uma nota: "))
    tupla = (nome, nota)
    lista.append(tupla)

def notas(ordenar):
    return ordenar[1]
lista.sort(key = notas, reverse=True)

for item in lista:
    print(item)
    
    
""" 
lista.sort(key=lambda x: x[1], reverse=True)

lambda é uma função anônima (sem nome), também chamada de função lambda.
x é cada elemento da lista.
x[1] ta falando pa pegar o elemento na posição 1 (nota)
"""








"""lista_tupla.append(nome)
lista_tupla.append(nota)"""

"""tupla = (nome,nota)
lista.append(tupla)"""
"""print(lista_tupla)
tupla = tuple(lista_tupla)
print(tupla)
print(lista)


for pos_nota in range(0, len(tupla)):
    if pos_nota % 2 == 1:
        lista_tupla.sort(reverse=True)
print(lista)"""


"""for pos_nota in range(0, len(lista)):
    if pos_nota % 2 == 1:
        for j in range(len(lista[pos_nota])-1):
            if lista[pos_nota][j] < lista[pos_nota][j+1]:
                aux = lista[pos_nota][j+1]
                lista[pos_nota][j+1] = lista[pos_nota][j]
                lista[pos_nota][j] = aux

        print(lista[pos_nota])"""
            
#aramazena o segundo em uma var aux
#atribui o valor do primeiro para o segundo
#atribui o valor do segundo para o primeiro