class Tarefa:
    def __init__(self, descricao, data):
        self.descricao = descricao
        self.data = data
        self.concluida = False

    def concluir_tarefa(self):
        self.concluida = True

    def exibir_detalhes(self):
        print(f'A tarefa {self.descricao} é do dia {self.data} e está com status'
              f'{"concluída" if self.concluida else "não concluída"}')


tarefa1 = Tarefa('Estudar Python', '16/08/2023')
tarefa1.exibir_detalhes()

tarefa1.concluir_tarefa()
tarefa1.exibir_detalhes()


