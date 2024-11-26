numeros = set([1,2,3,1,3,4])
print(numeros)
letras = set("abacaxi")
print(letras)
carros = set(("palio", "gol", "celta", "palio"))
print(carros)


linguagens = {"python", "java", "python"}
print(linguagens)
##para consumir os dados de um conjuto, deve se transformar ele para uma lista antes
numeros = list(numeros)

print(numeros[0])


carros = {"gol", "celta", "palio"}
for carro in carros:
    print(carro)


carros = {"gol", "celta", "palio"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



#Metodos do Set

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b))


conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))



conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))



conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))




sorteio = {1, 23}

print(sorteio.add(25))
print(sorteio.add(42))
print(sorteio.add(25))
sorteio.clear()
sorteio.copy()



numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.discard(1)
numeros.discard(45)


numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.pop()
numeros.pop()

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

numeros.remove(0)


numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
len(numeros)


numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
1 in numeros
10 in numeros