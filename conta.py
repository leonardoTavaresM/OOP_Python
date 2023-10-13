class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('construindo objeto... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('saldo {} do titular {}'.format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        self.extrato()

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta = Conta(123, 'Leonardo', 500.0, 1000.0)

conta2 = Conta(456, 'Mari', 300.0, 800.0)

conta.depositar(10)
conta.sacar(5)

print(conta.extrato())

# if __name__ == '__main__':
#     print('PyCharm')
