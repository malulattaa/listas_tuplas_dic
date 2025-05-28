lista = []


while True:
    num = int(input("Digite números da lista ou (000) para sair: "))
    
    if num == 000:
        break
    lista.append(num)

partes = int(input("deseja dividir a lista em quantas partes? "))
tamanho_lista = len(lista)
divisao = tamanho_lista//partes

sublista = [lista[i:i + divisao] for i in range(0, tamanho_lista, divisao)]
print(sublista)
