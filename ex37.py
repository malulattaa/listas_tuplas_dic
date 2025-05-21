""" 
Crie uma lista de palavras e remova as que tiverem menos de 4 letras
"""
palavras = []
letras = []
while True:
    p = input("Digite paravras ou (sair) para encerrar a execução: ")
    if p == 'sair' or p == 'SAIR':
        break
    palavras.append(p)
qtde = []

for i in range(len(palavras)):
    qtde.append(len(palavras[i]))

    if qtde[i] >= 4:
        letras.append(palavras[i])
        
print(letras)