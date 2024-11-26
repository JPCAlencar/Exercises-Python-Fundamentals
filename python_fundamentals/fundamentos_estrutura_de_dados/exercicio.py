# def soma_tupla(tupla):
#     return sum(tupla)

# if __name__ == "__main__":
#     entrada = input()
# # No "TODO", abaixo: Defina tupla para receber os números inteiros:
#     elementos = tuple(map(int, entrada.split()))
    
#     resultado = soma_tupla(elementos)
#     print(f"A soma dos elementos da tupla é: {resultado}")

# def elementos_comuns(lista1, lista2):

#     set1 = set(lista1)
#     set2 = set(lista2)

#     return list(set1.intersection(set2))

# # Leitura das listas
# lista1 = input().split()
# lista2 = input().split()
# lista = lista1 + lista2

# # Verifica se todas os elementos das listas podem ser convertidos para inteiros
# if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
#     lista1 = map(int, lista1)
#     lista2 = map(int, lista2)
#     comuns = elementos_comuns(lista1, lista2)
#     print(f"Elementos comuns às duas listas: {comuns}")
# else:
#     print("Entrada inválida.")



def contar_caracteres(string):

    contador = {}

    for caractere in string:
        if caractere in contador:
         contador[caractere] =+ 1
    else:
        contador[caractere] = 1

    
    return contador

entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)