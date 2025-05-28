""" 
crie um programa que tenha uma tupla totalmente 
preenchida com uma contagem por extensão, 
de zero até 20

seu programa deverá ler um número pelo teclado 
entre 0 a 20 e mostrá-lo por extensão
"""



"""tupla = (0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
extenso = ("zero","um", "dois", "tres", "quatro" , "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

num = int(input("Digite um número: "))
if num in tupla:
    print(extenso[num])
else:
    print("Número não está na lista")"""



#correção

extenso = ("zero","um", "dois", "tres", "quatro" , "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True: 
    num = int(input("Digite um número entre 0 e 20: "))
    if 0<= num <=20:
        break
    print("Tente Novamente")
    
print(f"Você digitou o número {extenso[num]}")

#perguntar se quer continuar e cotinuar colocando o numero que o usuario digitou