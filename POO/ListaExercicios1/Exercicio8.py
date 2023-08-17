class Sensor:
    def __init__(self, identificador, unidade):
        self.identificador = identificador
        self.unidade = unidade
        self.temperatura_atual = 0.0

    def atualizar_temperatura(self, temperatura: float):
        self.temperatura_atual = temperatura


    def exibir_leitura(self):
        print(f'A temperatura atual é de {self.temperatura_atual} graus {self.unidade}')


sensor1 = Sensor('Casa do cachorro', 'Celsius')
sensor1.exibir_leitura()
sensor1.atualizar_temperatura(22.0)
print(f'A temperatura atual do sensor da {sensor1.identificador} '
      f'é de {sensor1.temperatura_atual} graus {sensor1.unidade}')
