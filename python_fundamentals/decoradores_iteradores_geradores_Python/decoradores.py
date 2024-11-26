#função ainda sem o decorador
# def meu_decorador(funcao):
#     def envelope():
#         print("Faz algo antes de executar")
#         funcao()
#         print("Faz algo depois de executar")

#     return envelope

# def ola_mundo():
#     print("Olá mundo!")



# ola_mundo = meu_decorador(ola_mundo)
# ola_mundo()

#Exemplo com decorador "Onde so é preciso colocar o @ na função que deseja" fazendo com que não seja necessario escrever "ola_mundo = meu_decorador(ola_mundo)" com o @ ele ja faz isto automaticamente
# def meu_decorador(funcao):
#     def envelope():
#         print("Faz algo antes de executar")
#         funcao()
#         print("Faz algo depois de executar")

#     return envelope

# @meu_decorador
# def ola_mundo():
#     print("Olá mundo!")

# ola_mundo()



#Adiciona "*args" e "*kwargs" para que não seja necessario passar um valor especifico e sim passar um generico quando naão se sabe exatamente o que quer 
# def meu_decorador(funcao):
#     def envelope(*args, **kwargs):
#         print("Faz algo antes de executar")
#         funcao(*args, **kwargs)
#         print("Faz algo depois de executar")

#     return envelope

# @meu_decorador
# def ola_mundo(nome, idade=None):
#     if idade:
#         print(f"Olá mundo {nome}, e minha idade é: {idade}!")
#     else:
#         print(f"Olá mundo, {nome}")

# ola_mundo("João", idade=21)



#faz o def envolope quardar o proprio valor em resultado e retornar ele mesmo, para consegueir modificar a 'funcao' com .upper ou de qualquer outra maneira
# def meu_decorador(funcao):
#     def envelope(*args, **kwargs):
#         print("Faz algo antes de executar")
#         resultado = funcao(*args, **kwargs)
#         print("Faz algo depois de executar")
#         return resultado

#     return envelope

# @meu_decorador
# def ola_mundo(nome):
#     print(f"Olá mundo {nome}!")
#     return nome.upper()

# resultado = ola_mundo("João")
# print(resultado)


#o functools wrap, faz o ola_mundo retornar o nome dele mesmo certo
import functools
def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar")
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")
    return nome.upper()

resultado = ola_mundo("João")
print(resultado)
print(ola_mundo.__name__)