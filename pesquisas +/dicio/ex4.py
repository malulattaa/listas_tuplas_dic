dicio = {}
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
    i+=1
lista.append(dicio.copy())
for x in lista:
    for c, v in x.items():
        print(f"O campo {c} tem valor {v}")
print(f"O jogador {dicio['jogador']} jogou {dicio['partida']} partidas.")
for j in lista_gol:
    print(f"Na partida {k} fez {j}")
    soma += j
    k += 1
print(f"Total de {soma} gols")
