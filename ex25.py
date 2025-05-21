""" 
Solicite uma frase ao usu´ario e retorne uma lista com todas as palavras (use split)

#split
split() em Python é usado para dividir uma string em partes,
baseado em um separador (também chamado de delimitador). Ele retorna uma lista de substrings.

SINTAXE:
string.split(separador, maxsplit)

- separador (opcional): caractere ou string usada para dividir. Se for omitido, usa espaços em branco (espaço, tab, quebra de linha).

- maxsplit (opcional): número máximo de divisões. O restante da string permanece junto.
"""

frase = input("Digite uma frase: ")

palavras = frase.split()
print(palavras)