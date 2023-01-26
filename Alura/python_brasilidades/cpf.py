from validate_docbr import CPF

class Cpf:
    
    def __init__(self,documento):
        
        documento = str(documento)
        
        if self.cpf_eh_valido(documento):
            self.cpf = documento
            print('CPF Validado')
        else:
            raise ValueError('CPF Invalido')
    
    def __str__(self) -> str:
        return self.format_cpf()
    
    def cpf_eh_valido(self,documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            return False
    
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)    
    
