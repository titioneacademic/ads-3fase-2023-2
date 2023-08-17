class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        return 'Este animal emite um som'


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie='Cachorro')
        self.__raca = raca

    def obter_raca(self):
        return self.__raca

    def emitir_som(self):
        return 'Au au'


class Gato(Animal):
    def __init__(self, nome, pelagem):
        super().__init__(nome, especie='Gato')
        self.__pelagem = pelagem

    def obter_pelagem(self):
        return self.__pelagem

    def emitir_som(self):
        return 'Miau'


cao = Cachorro('Robson', 'Caramelo')
gato = Gato('Creatina', 'branca e amarela')

print(f'A gata {gato.nome} fala {gato.emitir_som()}. '
      f'\nSua sua pelagem é {gato.obter_pelagem()}')
print(f'O cão {cao.nome} fala {cao.emitir_som()}.'
      f'\nSua raça é {cao.obter_raca()}')
