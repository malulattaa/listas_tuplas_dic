""" 
Converta uma lista de temperaturas em Celsius para Fahrenheit com compreens˜ao
de listas.
"""

temperaturas = [18, 25, 40, 35, 16, -5]
celsius = [((x*1.8)+32) for x in temperaturas]
print(celsius)