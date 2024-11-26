nome = "João Pedro"
idade = "28"
profissao = "CEO Google"
linguagem = "Python"
saldo = 50.000000

dados = {"nome": "João Pedro", "idade" : 28}

print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {0} Idade: {1}" .format(nome, idade))
print("Nome: {0} Idade: {1}" .format(nome, idade))
print("Nome: {nome} Idade: {idade}" .format(nome = nome, idade = idade))
print("Nome: {nome} Idade: {idade}" .format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.7f}")
