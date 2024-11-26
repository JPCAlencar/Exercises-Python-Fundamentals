pessoa = {"nome": "João Pedro", "idade": 28}


pessoa = dict(nome="João Pedro", idade= 28)



pessoa["telefone"] = "3333-1234"

for i in pessoa.items():
    print(i)


print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

pessoa["nome"] = "Maria"
pessoa["idade"] = 18
pessoa["telefone"] = "9988-1781"
print(pessoa)



contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"},
        "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "1234-5678"},
        "chappie@gmail.com": {"nome": "Chappie", "telefone": "7895-5421"},
        "Melaine@gmail.com": {"nome": "Melaine", "telefone": "2554-9354"},
}

print(contatos["alencarjoaopedro385@gmail.com"]["telefone"])

for chave in contatos:
    print(chave, contatos[chave])


for chave, valor in contatos.items():
    print(chave, valor)

##metodos

contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"},
        "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "1234-5678"},
        "chappie@gmail.com": {"nome": "Chappie", "telefone": "7895-5421"},
        "Melaine@gmail.com": {"nome": "Melaine", "telefone": "2554-9354"},
}

contatos.clear()

contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"}}

copia = contatos.copy()
copia["alencarjoaopedro385@gmail.com"] = {"nome" : "Gui"}

print(contatos["alencarjoaopedro385@gmail.com"])
print([copia["alencarjoaopedro385@gmail.com"]])


print(dict.fromkeys(["nome", "telefone"]))
print(dict.fromkeys(["nome", "telefone"], "vazio"))

contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"}}

#contatos["chave"]

contatos.get("chave")
contatos.get("chave", {})
contatos.get("guilherme@gmail.com", {})

contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"}}

print(contatos.items())


contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"}}

print(contatos.keys())

contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"}}

print(contatos.pop("alencarjoaopedro385@gmail.com"))
print(contatos.pop("alencarjoaopedro385@gmail.com", "Não Encontrado"))


contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"}}

print(contatos.popitem())
#print(contatos.popitem())

contato = {'nome' : 'Guilherme', 'Telefone' : '3333-2221'}
contato.setdefault("nome", "Giovanna")
print(contato)

contato.setdefault("idade", 28)
print(contato)

contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"}}

contatos.update({"alencarjoaopedro385@gmail.com" : {"nome" : "Gui"}})
print(contatos)

contatos.update({"giovanna@gmail.com" : {"nome" : "Giovanna", "telefone" : "3322-8181"}})
print(contatos)


contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"},
        "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "1234-5678"},
        "chappie@gmail.com": {"nome": "Chappie", "telefone": "7895-5421"},
        "Melaine@gmail.com": {"nome": "Melaine", "telefone": "2554-9354"},
}

print(contatos.values())


contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"},
        "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "1234-5678"},
        "chappie@gmail.com": {"nome": "Chappie", "telefone": "7895-5421"},
        "Melaine@gmail.com": {"nome": "Melaine", "telefone": "2554-9354"},
}

resultado = "alencarjoaopedro385@gmail.com" in contatos
resultado = "megui@gmail.com" in contatos
resultado = "idade" in contatos["alencarjoaopedro385@gmail.com"]
resultado = "telefone" in contatos["giovanna@gmail.com"]

print(resultado)


contatos ={
        "alencarjoaopedro385@gmail.com": {"nome": "João Pedro", "telefone": "(22)99972-7320"},
        "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "1234-5678"},
        "chappie@gmail.com": {"nome": "Chappie", "telefone": "7895-5421"},
        "Melaine@gmail.com": {"nome": "Melaine", "telefone": "2554-9354"},
}


del contatos["alencarjoaopedro385@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]
print(contatos)