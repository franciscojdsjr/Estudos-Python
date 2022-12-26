class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0
        
    @property
    def likes (self):
        return self.__likes    

    @property
    def nome (self):
        return self.__nome
    
    @property
    def ano (self):
        return self.__ano
    
    @property
    def duracao (self):
        return self.__duracao

    def dar_like (self):
        self.__likes += 1
    
    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome.title()
    
        
class Serie:
    
    def __init__(self, name, ano, temporadas):
        self.__name = name.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0
        
    @property
    def likes (self):
        return self.__likes    

    @property
    def nome (self):
        return self.__nome
    
    @property
    def ano (self):
        return self.__ano
    
    @property
    def duracao (self):
        return self.__duracao

    def dar_like (self):
        self.__likes += 1
    
    @nome.setter
    def nome(self,novo_nome):
        self.nome = novo_nome.title()