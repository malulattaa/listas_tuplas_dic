""" 
Crie uma função recursiva que diga se uma string é igual a ela mesma ao contrário.
Ex: eh_palindromo("arara") → True

"""

def palindromo(string):
    
    if len(string) <= 1:
        return True
    if string[-1] != string[0]:
        return False
    return palindromo(string[1:-1])



print(palindromo("musica"))