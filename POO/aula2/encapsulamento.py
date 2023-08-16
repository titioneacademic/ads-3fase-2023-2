class ContaBancaria:
    def __init__(self, saldo: int):
        self._saldo = saldo

    def depositar(self, valor: int):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor: int):
        if 0 < valor <= self._saldo:
            self._saldo -= valor

    def get_saldo(self):
        return self._saldo


conta_1 = ContaBancaria(10000)

conta_1.depositar(5000)
conta_1.sacar(8000)
conta_1._
print(f'A Laura comprou uma moto de R$8000,00 e '
      f'ficou com saldo de R${conta_1.get_saldo()},00 ')
