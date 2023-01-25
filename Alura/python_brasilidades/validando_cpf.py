from validate_docbr import CPF
from cpf import Cpf




cpf = CPF()

print(cpf.validate('01327740460'))


documento = 10171921461

objeto_cpf = Cpf(documento)

print(objeto_cpf)

#tamanho_cpf = len(str(cpf))
#print(tamanho_cpf)