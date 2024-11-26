class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, marcha=1):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha

    def buzinar(self):
        print("Plim plim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm...")

    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha...")
        if nro_marcha > self.marcha:
            self.marcha = nro_marcha
            print(f"Marcha trocada para {self.marcha}.")
        else:
            print("Não foi possível trocar a marcha, escolha uma marcha maior.")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# Criando as bicicletas
b1 = Bicicleta("vermelha", "caloi", 2022, 600, 5)
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189, 3)
Bicicleta.buzinar(b2)
print(b2.cor)
print(b2)

# Testando troca de marcha
b1.trocar_marcha(3)
b1.trocar_marcha(6)
