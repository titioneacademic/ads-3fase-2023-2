class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco * produto.quantidade
        return total

    def mostrar_itens(self):
        if len(self.produtos) > 0:
            for i in self.produtos:
                print(f'Item {i.nome} quantidade {i.quantidade} valor R${i.preco}.')
        else:
            print('Não existem itens no carrinho.')


carrinho = CarrinhoDeCompras()
prod1 = Produto('Cadeira', 500.00, 10)
prod2 = Produto('Café', 270.00, 120)
carrinho.adicionar_produto(prod1)
carrinho.adicionar_produto(prod2)
carrinho.mostrar_itens()
print(f'O valor total do carrinho é R${carrinho.calcular_total()}')
