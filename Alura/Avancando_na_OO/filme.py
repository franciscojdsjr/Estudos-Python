class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0
        
    @property
    def likes (self):
        return self._likes    

    @property
    def nome (self):
        return self._nome
    
    @property
    def ano (self):
        return self._ano
    
    @property
    def duracao (self):
        return self._duracao

    def dar_like (self):
        self._likes += 1
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
        
        
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas
        
