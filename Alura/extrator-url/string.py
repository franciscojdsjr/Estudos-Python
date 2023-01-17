class Soma:
    
    def __init__(self,a,b):
         self.a = a
         self.b = b
         self.validacao(a,b)
         print('Soma é {}'.format(a+b))
         
    def __str__(self) -> str:
        
        return'Soma é {}'.format(self.a+self.b)
    
    
    def validacao(self,a,b):
         if type(a) == int and type(b) == int:
             True
         else:
             raise ValueError('Devem ser usado numeros como parametro')



resultado = Soma(10,5)
print(resultado)