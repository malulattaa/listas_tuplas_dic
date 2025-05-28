tupla = ('lapis', 'faca', 'garfo', 'prato', 'copo', 'mosca')
vogal = 'aeiou'

for i in tupla:
    for j in vogal:
        if j in i:
            print(f" Na palavra {i} temos {j}")