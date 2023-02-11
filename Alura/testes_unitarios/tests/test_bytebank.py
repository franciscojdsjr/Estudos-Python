from bytebank.codigo import Funcionarios
import pytest
from pytest import mark

class TestClass:
    
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '06/02/2000' #given - contexto
        esperado = 23
        
        funcionario_teste = Funcionarios('Francisco Junior',entrada, 1111)
        
        resultado = funcionario_teste.idade() #when ação
        
        assert resultado == esperado #then - desfecho

    def test_quando_sobrenome_recebe_Francisco_Junior_deve_retornar_apenas_Junior(self):
        entrada = 'Francisco Junior' #given
        esperado = 'Junior'
        francisco = Funcionarios(entrada,'29/12/1993',5000) 

        resultado = francisco.sobrenome() #when

        assert resultado == esperado #then
        
    def test_quando__decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada = 100000 #given
        esperado = 90000
        salario = Funcionarios('Paulo Bragança','29/12/1993',entrada)
        
        resultado = salario.decrescimo_salario() #when
        
        assert resultado == esperado #then 
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 #given
        esperado = 100
        bonus = Funcionarios('Francisco','29/12/1993',entrada)
        
        resultado = bonus.calcular_bonus() #when

        assert resultado == esperado #then
    
    @mark.calcular_bonus 
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000 #given
            bonus = Funcionarios('Francisco','29/12/1993',entrada)

            resultado = bonus.calcular_bonus() #when

            assert resultado #then
    