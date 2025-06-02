"""Objetivo: Receba uma lista de números e retorne a média dos números pares. Use uma função para filtrar os pares e outra para calcular a média."""


def pares(numeros):
    par = [x for x in numeros if x % 2 == 0]
    return par

def media_pares(lista):
    media = sum([x for x in pares(lista)]) / len([x for x in pares(lista)]) if any(x % 2 == 0 for x in pares(lista)) else 0
    return media
print(media_pares([1, 3, 5])) 