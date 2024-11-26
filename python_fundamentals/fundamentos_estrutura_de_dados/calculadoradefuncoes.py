for n in range (0, 2):
    int(input("Digite um número para a operação: "))

operação = str(input("Digite uma operação:"))

def somar(a,b):
    return a+b

def exibir_resultado(a,b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)