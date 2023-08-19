class Data:
    
    def __init__(self) -> None:
        self.dia = int(input('Digite o Dia: '))
        self.mes = int(input('Digite o Mês: '))
        self.ano = int(input('Digite o Ano: '))
    
    def formatada(self):
        formato = int(input('Qual formato de Data deseja? \n 1. dd/mm/aaaa\n 2. mm-dd-aaaa\n 3. aaaa-mm-dd\nDigite a opção correspondente: '))
        separador = input('digite o separador de data desejado: ')
        if formato == 1:
            print('{0}{3}{1}{3}{2}'.format(self.dia,self.mes,self.ano,separador))
        elif formato == 2:
            print('{0}{3}{1}{3}{2}'.format(self.mes,self.dia,self.ano,separador))
        elif formato == 3:
            print('{0}{3}{1}{3}{2}'.format(self.ano,self.mes,self.dia,separador))
        else:
            print('Digite uma opção valida')
        
        