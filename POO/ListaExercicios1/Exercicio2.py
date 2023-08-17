class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__disciplinas = []

    def adiciona_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def mostrar_disciplinas(self):
        return self.__disciplinas


aluno = Aluno('Gedaías', 52)
aluno.adiciona_disciplina('Desenvolvimento Web')
aluno.adiciona_disciplina('LPA')
print(f'O(a) aluno(a) {aluno.nome} cursa as disciplinas {", ".join(aluno.mostrar_disciplinas())}')
