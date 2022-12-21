class Conta:
    
    def __init__(self,numero,titular,saldo,limite) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print('O saldo de {} do titular {} e possui limite autorizado de {}'.format(self.saldo, self.titular, self.limite))
        
    def depositar(self,valor):
        self.saldo += valor
    
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saque invalido, seu saldo é de {} e você tentou sacar {}'.format(self.saldo,valor))
