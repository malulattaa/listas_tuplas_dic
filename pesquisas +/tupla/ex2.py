"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do CAAMPEONATO bRASILEIRO DE fUTEBOL, na ordem de colocação. Depois mostra:
    a) apenas os 5 primeiros colocados 
    b) os ultimos 4 colocados da tabela
    c) uma lista com os times em ordem alfabetica (soted?)
    d) em que posição na tabela está o time da chapecoense"""
    
time = ("Palmeiras", "Flamengo", "Chapecoense", "Vasco", "Inter", "Fluminense", "Botafogo", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Bragantino", "Ceara", "Mirassol", "Atlético MG", "Fortazela", "Santos", "Juventude", "Sport Recife", "Grêmio")

print(time[0:6])
print(time[-5:])
print(sorted(time))
for pos in range(0, len(time)):
    if time[pos] == "Chapecoense":
        print(f"{time[pos]} está na posição {pos+1}")
