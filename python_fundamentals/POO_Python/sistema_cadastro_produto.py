class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def valor_total(self):
        self.valor = self.preco * self.quantidade_em_estoque
        return self.valor


    def __str__(self):
        return f"{self.nome}: {self.valor_total():.2f}"
    


p1 = Produto("Lenovo ThinkPad", 1500, 800)
print(p1)