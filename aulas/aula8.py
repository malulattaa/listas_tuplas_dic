lista = [1,2,3,4,5]

#PESQUISAR: map, filter, reduce(?)

quadrado =[num**2 for num in lista]
print(quadrado)

pares = [x for x in lista if x % 2 ==0]
print(pares)

x = 10
y = 20

#def nome_funcao():
#nome da função deve ter relação com o que ela vai fazer


#depois da palavra pass, nada é executado (palavra reservada para quando nao se sabe extamente oq aquela função ira realizar)
def soma():
    soma = 2 + 2
#oq é declarado dentro da função (ou estrutura condicional), só existe dentro dela (escopo local)
#qnd criada fora, é escopo global (ainda nao - ver isso aq), pode ser visto dentro e fora 
soma() #chamando função
#parenteses agrupa os parametros

#procedimento,pega na função e ela morre dentro dela (?) prossegure

def soma(num1, num2):
    return num1 + num2
resul_soma = soma(5,2)
print(f"soma: {resul_soma}")

def sub(num1, num2):
    return num1 - num2
resul_sub = sub(5,2)
print(f"subtração = {resul_sub}")

def mult(num1, num2):
    return num1 * num2
resul_mult = mult(5,2)
print(f"multiplicação = {resul_mult}")

def divisao(num1, num2):
    return num1/num2
resul_div = divisao(5,2)
print(f"divisão = {resul_div}")

def exp(num1, num2):
    return num1**num2
#resul_exp= exp(5,2)
print(f"elevado = {exp(6,2)}")


