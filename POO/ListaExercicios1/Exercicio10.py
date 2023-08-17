class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
        else:
            print('Quantidade em estoque inferior à quantidade retirada')

    def calcular_total(self):
        return self.preco * self.quantidade



prod1 = Produto('Camisa', 127.50, 50)
prod1.adicionar_estoque(4)
prod1.remover_estoque(55)
print(f'O valor total do item {prod1.nome} é de {prod1.calcular_total()}')
