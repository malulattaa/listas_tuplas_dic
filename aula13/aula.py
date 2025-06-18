def minha_funcao(a, b):
    soma = a + b
    
#parametros obrigatorios, nao tem como chamar a func sem passar valor a eles

def minha_funcao(a, b = 1):
    soma = a + b
    
#b  é opcional, se eu n passar nada na hora de chamar, ele assume 1

#passar mts parametros para dentro de uma func não é bom mas pode acontecer

#nao pode colocar parametros opcionais no meio de paraemtros obrigatorios
#ele vai explorar isso

#args sempre vai ter um * e a palavra args (*args)
#são convenções em python que permitem que funções recebam um numero variavel de parametros

def minha_funcao(a, b, *args):
    print(f"Argumentos recebidos: {args}")

#para ter acesso em cada um dos parametros:
    for arg in args:
        print(f"- {arg}")

minha_funcao(2,3,5,6,[1,3,4])
#pode passar string tb
#args retorna uma tupla


def minha_funcao(a, b, *args):
    print(f"Argumentos recebidos: {args}")

#para ter acesso em cada um dos parametros:
    for arg in args:
        print(f"- {arg}")

minha_funcao(2,3,5,6,[1,3,4], [2, 3, [1, 2, 3]])




#funcao para contar num de sublistas de um uma lista (utilizar # isinstance)
#meu jeito
def minha_funcao(*args):

#para ter acesso em cada um dos parametros:
    sub = 0
    for arg in args:
        if isinstance(arg, list):
            for sub in arg:
                sub += 1 
            return sub 
        

minha_funcao(2,3,5,6,[1,3,4], [2, 3, [1, 2, 3]])

print("")
print("")
#correção
#funcao normal

