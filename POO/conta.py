class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposito(self, valor):
        self.saldo += valor
        print("Saldo atual é de R$ {}".format(self.saldo))

    def saque(self, valor):
        self.saldo -= valor

    def extrato(self):
        print("Olá, {} seu saldo é de {}".format(self.titular, self.saldo))