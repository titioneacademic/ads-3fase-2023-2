class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

    def atualizar_ano_publicacao(self, ano):
        self.ano = ano

    def exibir_detalhes(self):
        print(f'Livro: {self.titulo}, autor {self.autor} \n'
              f'Ano de publicação {self.ano} e gênero {self.genero}')

livro1 = Livro('Lord of the rings', 'J.R.R. Tolkien', '1954', 'Fantasia')
livro1.exibir_detalhes()
livro1.atualizar_ano_publicacao('2023')
livro1.exibir_detalhes()

