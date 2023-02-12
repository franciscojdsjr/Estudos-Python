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
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]
    
    def _cargo_executivo (self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        if self.sobrenome() in sobrenomes:
            return True
    
    def decrescimo_salario(self):
          if (self.salario >= 10000) and (self._cargo_executivo() == True):
              decrescimo = self._salario * 0.1
              self._salario = self._salario - decrescimo
              return self._salario
        
    
    def calcular_bonus(self):
       valor = self._salario * 0.1
       if valor > 1000:
           raise Exception('O Salário é muito alto para receber bônus')
       else:
           return valor
       
    def __str__(self):
        return 'Funcionario(Nome: {}, Data de Nascimento: {}, Salario: R$:{})'.format(self._nome,self._data_nascimento,self.salario) 
        
        