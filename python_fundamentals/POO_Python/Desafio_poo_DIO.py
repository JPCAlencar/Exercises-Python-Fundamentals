# class Calculadora:
#     def __init__(self):
#         self.num1 = int(input())
#         self.num2 = int(input())

#     def soma(self):
#         return self.num1 + self.num2

# calc = Calculadora()

# resultado = calc.soma()
# print(resultado)



# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def __str__(self):
#         return f"Nome : {self.nome} Idade: {self.idade}"
    

# # Entrada do usuário
# nome = input()
# idade = int(input())

# # TODO: Crie uma instância da pessoa:
# p = Pessoa(nome, idade)
# #TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
# print(p)


# class ConversorTemperatura:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def celsius_para_fahrenheit(self):
#        fahrenheit = (self.celsius * 9/5) + 32
#        return fahrenheit


# celsius = float(input())

# conversor = ConversorTemperatura(celsius)

# fahrenheit = conversor.celsius_para_fahrenheit()
# print(fahrenheit)


class Calculadora:
    def __init__(self):
        self.num1= 0
        self.num2= 0

    def obter_numeros(self):
        self.num1 = float(input("Digite o 1° número:"))
        self.num2 = float(input("Digite o 2° número:"))

    def somar(self):
        return self.num1 + self.num2 

    def subtrair(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2 

    def dividir(self):
        if self.num2 == 0:
            return "Erro: divisão por 0 não é permitida"
        return self.num1 / self.num2
        

print("----------Bem vindo a calculadora----------")
calc = Calculadora()
opcao = -1
while opcao != 0:
    print("Escolha uma operação:")
    opcao = int(input(" [1] Somar \n [2] Subtrair \n [3] Multiplicar \n [4] Dividir \n [0] Sair"))
    if opcao in [1,2,3,4]:
        calc.obter_numeros()
        if opcao == 1:
            resultado = calc.somar()
            print(f"O resultado da soma é: {resultado}")
        elif opcao == 2:
            resultado = calc.subtrair()
            print(f"O resultado da subtração é: {resultado}")
        elif opcao == 3:
            resultado = calc.multiplicar()
            print(f"O resultado da multiplicação é: {resultado}")
        elif opcao == 4:
            resultado = calc.dividir()
            print(f"O resultado da divisão é: {resultado}")
    elif opcao == 0:
        print("Saindo do sistema")
    else:
        print("Opção invalida, digite novamente")
print("Programa Encerrado.")