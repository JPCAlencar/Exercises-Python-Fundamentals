# def exibir_mensagem():
#     print("Olá Mundo!")

# def exibir_mensagem_2(nome):
#     print(f"Seja bem vindo {nome}!")

# def exibir_mensagem_3(nome = "Anônimo"):
#     print(f"Seja bem vindo {nome}!")

# exibir_mensagem()
# exibir_mensagem_2(nome="Guilherme")
# exibir_mensagem_3()
# exibir_mensagem_3(nome="Chappie")

# def calcular_total(numeros):
#     return sum(numeros)

# def retorna_antecessor_e_sucessor(numero):
#     antecessor = numero - 1
#     sucessor = numero + 1

#     return antecessor, sucessor

# def func_3(): #Não tem o valor de return explicito, ai por padrão volta NONE
#     print("Olá Mundo")

# print(f"O total da operação é: {calcular_total([10, 20, 34])}")
# print(retorna_antecessor_e_sucessor(10))
# numero = 10
# antecessor, sucessor = retorna_antecessor_e_sucessor(numero)
# print(f"O sucessor de {numero} é {sucessor} e o antecessor é {antecessor}")
# print(func_3())


# def salvar_carro(marca, modelo, ano, placa):
#     print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")#Melhor de se usar
# salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# def exibir_poema(data_extenso, titulo, *args, **kwargs):
#     texto = "\n".join(args)
#     meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
#     mensagem = f"{data_extenso}\n\n{titulo}\n\n{texto}\n\n{meta_dados}"
#     print(mensagem)

# exibir_poema("Segunda-feira, 14 de Outubro de 2024","Poema do Python", "Zen of Python", "Beautiful is better than ugly.", "Suck my dick.", autor = "Tim Peters", ano =1999, editora = "Mundo Livro")

#Parametros posicionais

#Valores por posição
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1989, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#Valores somente por chave : valor
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


#Pode ser posicional quanto por chave : valor, porem, não pode ser nenhum especifico
def criar_carro(modelo, ano, placa, /,*, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#Objetos de primeira classe
def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def exibir_resultado(a,b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é de = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

op = somar

print(op(1,20))

#Escopo Global e Local (Sempre evitar de usar o Global)

salario = 2000

def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_bonus = salario_bonus(500, lista)
print(salario_bonus)
print(lista)