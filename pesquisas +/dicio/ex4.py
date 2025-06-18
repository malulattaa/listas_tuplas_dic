"""dicio = {}
lista = []
lista_gol = []

i = 1
k = 1
soma = 0
dicio['jogador'] = input("Digite o nome do jogador: ")
dicio['partida'] = int(input(f"Quantas partidas {dicio['jogador']} jogou? "))

while i < dicio['partida'] + 1:
    dicio['gols'] = int(input(f"Quantos gols na partida {i}? "))
    lista_gol.append(dicio['gols'])
    dicio['gols'] = lista_gol
    i+=1
lista.append(dicio.copy())

for campo, valor in dicio.items():
    print(f"O campo {campo} tem valor {valor}")
    

print(f"O jogador {dicio['jogador']} jogou {dicio['partida']} partidas.")
for j in lista_gol:
    print(f"Na partida {k} fez {j}")
    soma += j
    k += 1
print(f"Total de {soma} gols")"""

#correção

jogador = {}
partidas = []
time = []

while True:
    jogador['nome'] = input("Nome do jogador: ")
    
    tot = int(input(f"Quantas partidas o {jogador['nome']} jogou?"))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"Quantos gols na partida {c}? ")))
        
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = input("Quer continuar (S/N): ")
        if continuar in 'SN':
            break
        print("Erro")
    if continuar == 'N':
        break
print("")
print('cod', end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print("")
for k,v in enumerate(time):
    print(f"{k:>4}", end = "")
    for d in v.values():
        print(f"{str(d):<15}", end ='')
    print("")
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 parar parar)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"erro")
    else:
        print(f"Levantamento do jogador {time[busca]['nome']}: ")
        for i, g in enumerate(time[busca]['gols']): 
            print(f"no jogo {i+1} fez {g} gols")