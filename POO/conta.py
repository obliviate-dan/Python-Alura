'''
from conta import Conta
conta2 = Conta(42, "Lupim", 264.34, 500)
conta = Conta(934, "Fred", 549.54, 2500)
'''
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposito(self, valor):
        self.__saldo += valor
        print("Saldo atual é de R$ {}".format(self.__saldo))

    def saque(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print("Olá {}, seu saldo é de R${}".format(self.__titular, self.__saldo))

    def transferir(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    def get_saldo(self):
        return self._saldo

    def get_titular(self):
        return self._titular

    def get_limite(self):
        return self._limite

    def set_limite(self, limite):
        self._limite = limite