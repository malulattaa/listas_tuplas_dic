def eh_par(n):
    return n % 2 == 0

def dobrar_se_par(n):
    if eh_par(n):
        return n * 2
    return n

print(dobrar_se_par(4)) #8
print(dobrar_se_par(5)) #nao passo pela multiplicação por 2 pq n é par, ent retorna ele mesmo