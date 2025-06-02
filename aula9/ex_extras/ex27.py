"""Objetivo: Dado uma lista de palavras, retorne as palavras com número par de letras e que contenham a letra "a"."""

def par_letra(lista):
    return [x for x in lista if len(x) % 2 == 0]

def filtrar_palavras(lista):
    return [x for x in par_letra(lista) if 'a' in x ]





print(filtrar_palavras(["casa", "sol", "barco", "lua", "azeite", "café"]))