class Conta:
    def __init__(self, num_agencia, saldo = 0):
        self._saldo = saldo
        self.num_agencia = num_agencia
    def depositar(self, valor):
        self._saldo += valor
    def sacar(self, valor):
        self._saldo -= valor
    def extrato(self):
        return self._saldo

conta = Conta("001", 100)
conta.depositar(100)
print(conta.extrato()) 