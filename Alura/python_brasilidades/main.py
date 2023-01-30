from datetime import datetime, timedelta
from datas_br import DatasBr

##print(datetime.today())


cadastro = DatasBr()

print(cadastro.mes_cadastro(), cadastro.dia_semana())
print(cadastro)

