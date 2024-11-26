def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

# Usando o gerador em um loop
print("Usando o for:")
for i in meu_gerador(numeros=[1, 2, 3, 4]):
    print(i)

# Convertendo o gerador para uma lista usando list()
print("\nUsando list():")
resultado = list(meu_gerador([1, 2, 3, 4]))
print(resultado)
