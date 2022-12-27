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

    def dar_likes (self):
        self._likes += 1
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome.title()
    
    def __str__ (self):
        return f'Nome: {self._nome}, Ano: {self._ano}, Likes: {self._likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    ##quando fazemos isso substituimos o metodo original 
    def __str__ (self):
        return f'Nome: {self._nome}, Ano: {self._ano}, Duração: {self._duracao}, Likes: {self._likes}'
   
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas
    
    ##quando fazemos isso substituimos o metodo original
    def __str__ (self):
        return f'Nome: {self._nome}, Ano: {self._ano}, Temporadas {self._temporadas}, Likes: {self._likes}'
        
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()
filmes_e_series = [vingadores, atlanta]


for programa in filmes_e_series:
    print(programa)
 
