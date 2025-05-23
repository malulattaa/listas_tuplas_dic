numeros = []

while True:
    entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")
    if entrada.lower() == "sair":
        break
    try: #Tente converter entrada para um inteiro (int(entrada)).
        valor = int(entrada)
        numeros.append(valor) #Se der certo, armazene em valor e adicione à lista numeros.
    except ValueError: #caso não digite sair nem um numero inteiro
        print("Digite um número inteiro válido ou 'sair'.")
