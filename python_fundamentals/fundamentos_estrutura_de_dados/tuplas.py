frutas = ("laranja", "pera", "uva",)

letras = tuple("Python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)

frutas[0]
frutas[2]
frutas[-1]
frutas[-3]

matriz =(
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

print(matriz[0])
print(matriz[0][1])
print(matriz[0][-1])

tupla = ("p", "y", "t", "h", "o", "n")

tupla[2:]
tupla[:2]
tupla[1:3]
tupla[0:3:2]
tupla[::]
tupla[::-1]

carros = ("Gol", "Celta", "Palio")

for carro in carros:
    print(carro)



carros = ("Gol", "Celta", "Palio")

##indice para enumerar e saber quantos itens tem na tupla ou lista.
for indice, carro in enumerate(carros):
    print(f"{indice}: {carros}")



cores = ("vermelho", "azul", "verde", "azul",)

cores.count("vermelho")
cores.count("azul")
cores.count("verde")

linguagens = ("python", "js", "c", "java", "csharp",)

linguagens.index("java")
linguagens.index("python")

linguagens = ("python", "js", "c", "java", "csharp",)

len(linguagens)