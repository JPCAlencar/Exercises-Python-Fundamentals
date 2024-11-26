class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
    @classmethod
    def criar_apartir_dtnasc(cls, ano, mes, dia, nome):
          idade = 2024 - ano
          return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
         return idade >= 18


# p = Pessoa("João Pedro", 21)
# print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_dtnasc(2003, 10, 20, "João Pedro")
print(p2.nome, p2.idade)


print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(10))