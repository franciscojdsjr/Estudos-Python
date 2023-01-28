from validacao_documento import Documento

exemplo_cnpj = '87478499000125'
exemplo_cpf = '01327740460'
##cnpj = CNPJ()

##print(cnpj.validate(exemplo_cnpj))

documento_cnpj = Documento.criar_documento(exemplo_cnpj)
documento_cpf = Documento.criar_documento(exemplo_cpf)

print(documento_cnpj)
print(documento_cpf)