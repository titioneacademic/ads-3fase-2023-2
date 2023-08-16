class Animal:
    def falar(self):
        pass


class Catioro(Animal):
    def falar(self):
        return 'Au Au'


class Gatineo(Animal):
    def falar(self):
        return 'Miaau'


def animal_falando(animal):
    print(animal.falar())


cao = Catioro()
gato = Gatineo()

animal_falando(cao)
animal_falando(gato)
