from bytebank.codigo import Funcionarios

class TestClass:
    
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '06/02/2000' #given - contexto
        esperado = 23
        
        funcionario_teste = Funcionarios('Francisco Junior',entrada, 1111)
        
        resultado = funcionario_teste.idade() #when ação
        
        assert resultado == esperado #then - desfecho

    def test_quando_sobrenome_recebe_Francisco_Junior_deve_retornar_apenas_Junior(self):
        entrada = 'Francisco Junior'
        esperado = 'Junior'
        francisco = Funcionarios(entrada,'29/12/1993',5000)

        resultado = francisco.sobrenome()

        assert resultado == esperado