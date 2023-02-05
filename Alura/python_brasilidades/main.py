from datetime import datetime, timedelta
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

##print(datetime.today())


##datas = DatasBr()
##
##print(datas.tempo_cadastro())

#asims

cep = 57081760
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)