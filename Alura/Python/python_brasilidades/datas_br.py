from datetime import datetime,timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def mes_cadastro(self):
        meses_do_ano = [
            'janeiro','fevereiro','março',
            'abril','maio','junho',
            'julho,agosto,setembro',
            'outubro','novembro','dezembro']
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dias_semana = [
            'segunda','terça','quarta','quinta',
            'sexta','sabado','domingo'
        ]
        dia_semana = self.momento_cadastro.weekday() 
        return dias_semana[dia_semana]
    
    def format(self):
        formato_br = datetime.strftime(self.momento_cadastro,'%d/%m/%Y %H:%M:%S')
        return formato_br
        
    def __str__(self) -> str:
        return self.format()
    
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - (self.momento_cadastro - timedelta(days = 1, hours = 20))
        return tempo_cadastro
