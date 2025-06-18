def soma(a,b,c):
    pass

soma(c=2, a=3, b=4)

def funcao_completa(par_obgt, *args, **kwargs):
#lista de parametros nomeados: kwargs
    print(f"Parâmetro obgt : {par_obgt}")
    print(f"Args extras : {args}")
    print(f"Kwargs extras : {kwargs}")
    
#exemplo de uso

funcao_completa("valor1", "extra1", "extra2", nome="beto", idade = 30)

#implementar uma calculadora que leia 2 tipo de operações(soma, mult), passar uma listar de números (quantos numeros eu quero passar pra minha função para que ele faça a soma oum[ mult de toda a lista])
#exibir_detalhes = True, caso for false exibir resultado final