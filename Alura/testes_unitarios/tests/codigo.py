from datetime import date
from datetime import datetime

class Funcionarios:
    
    def __init__(self,nome,data_nascimento,salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def salario(self):
        return self._salario
    

    def idade(self):
        ano_atual = date.today().year
        nascimento = datetime.strptime(self._data_nascimento, '%d/%m/%Y').date().year
        return ano_atual - nascimento

    def sobrenome(self):
        pass
    
    def calcular_bonus(self):
       valor = self._salario * 0.1
       if valor > 1000:
           valor = 0
       else:
           return valor
       
    def __str__(self):
        return 'Funcionario(Nome: {}, Data de Nascimento: {}, Salario: R$:{})'.format(self._nome,self._data_nascimento,self.salario) 
        
        