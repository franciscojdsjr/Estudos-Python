class Conta:
    
    def __init__(self,numero,titular,saldo,limite) -> None:
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print('O saldo de {} do titular {} e possui limite autorizado de {}'.format(self.__saldo, self.__titular, self.__limite))
        
    def depositar(self,valor):
        self.__saldo += valor
        
    def __pode_sacar(self,valor):
        limite_disponivel = (self.__saldo + self.__limite)
        return valor <= limite_disponivel
    
    def sacar(self,valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('Saque não realizado, seu saldo é de {}, seu limite de {} e você tentou sacar {}'.format(self.__saldo,self.__limite,valor))
            
    def transferir(self,valor,destino):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('Transferencia não realizada, seu saldo é de {}, seu limite de {} e você tentou transferir {}'.format(self.__saldo,self.__limite,valor))
        destino.__saldo += valor
        print('Você transferiu: {} para a conta de {} e seu saldo agora é {}'.format(valor,destino.titular,self.__saldo))
        
    @property    
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite 
        
    @staticmethod
    def codigo_banco():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}    
        
