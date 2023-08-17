class ContaBancaria:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def realizar_deposito(self, valor):
        self.saldo += valor


conta = ContaBancaria(123456, 'Tião')
print(f'A conta de {conta.titular} está aberta com saldo de R${conta.saldo}')
conta.realizar_deposito(127000.14)
print(f'{conta.titular} está rico, sua conta está com saldo de R${conta.saldo}')
