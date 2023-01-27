from validate_docbr import CNPJ

exemplo_cnpj = '353798380000112'
cnpj = CNPJ()

print(cnpj.validate(exemplo_cnpj))