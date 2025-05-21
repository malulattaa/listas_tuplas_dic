""" 
Crie uma fun¸c˜ ao que recebe uma lista e retorna uma nova lista com apenas os
elementos ´ unicos.

"""
nomes = ['maria', 'luisa', 'maria', 'gabi', 'luisa', 'matheus', 'gabi']

def sem_repetidos(nomes):
    return list(set(nomes))

print(sem_repetidos(nomes))