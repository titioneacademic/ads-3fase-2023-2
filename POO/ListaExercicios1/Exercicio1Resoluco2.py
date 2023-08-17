class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def remover_produto(self, produto: Produto):
        self.produtos.remove(produto)

    def calcula_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco * produto.quantidade
        return total


prod = Produto('Camisa', 13, 114)
prod2 = Produto('Pelucia', 10.90, 240)

estoque = Estoque()
estoque.adicionar_produto(prod)
estoque.adicionar_produto(prod2)

print(f'O valor total do estoque é de R${estoque.calcula_total()}')
