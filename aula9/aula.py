
#resultado = 0
# nao é escopo global, mas é visivel fora e dentro da função
#se tivesse um resultado = 3, dentro de uma função, elas seriam variaveis diferentes que ocupam espaços diferentes na memoria 
#escopo global tem que utilizar a variavel globals (devem ser evitado para nao ocorrer o risco de alterarr uma variavel de forma acidental)

def soma(x,y):
    return x + y

def sub(x,y):
    return x - y
#td que esta apos a palavra return não sera executado
def mult(x,y):
    return x * y

def div(x,y):
    
    if y > 0:
        return x / y
    print("Y não pode ser 0")
    #possivel erro: divisao por 0
    
    
h = soma(2, 3) ** 2
#primeiro retorna a soma dos valores
#leva ao quadrado e vai pra linha seguinte
h3 = sub(2, 3)
h4 = mult(2, 3)
h5 = div(2, 3)
#podem ser usadas para outra coisa