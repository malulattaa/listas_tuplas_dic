""" Crie uma fun¸c˜ao que agrupe palavras por tamanho em um dicion´ario. """


def agrupar(palavras):
    agrupar = {}
    for i in palavras:
        tamanho = len(i)
        if tamanho not in agrupar:
            agrupar[tamanho] = [i]
        else:
            agrupar[tamanho].append(i)
    return agrupar

palavras = ["mãe", "sol", "vento", "céu", "lua", "flor"]
dicio = agrupar(sorted(palavras))
for c, v in dicio.items():
    print(f"{c} - {v}")

        