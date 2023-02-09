from codigo import Funcionarios
from datetime import datetime


#func = Funcionarios('Francisco','29/12/1993','5000')
##print(func.idade())
#print(func.idade())
##


def teste_idade():
    funciorio_teste = Funcionarios('Teste','06/02/2000','1158')
    print('Teste = {}'.format(funciorio_teste.idade()))
    

teste_idade()
    
    
    
# A importância da utilização de um ambiente virtual em projetos Python e como criar um através do comando 
# python3 -m venv venv, 
# ativando-o em seguida com o comando 
# source venv/bin/activate;
#testes