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

class Playlist():
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas
        
    def __getitem__(self,item):
        return self._programas[item]
        
    @property
    def listagem (self):
        return self._programas

    @property
    def tamanho (self):
        return len(self._programas)


    
        
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
pantera_negra = Serie('Pantera Negra', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()                                    
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'O tamanho da minha playlist é: {playlist_fim_de_semana.tamanho}')

for programa in playlist_fim_de_semana:
    print(programa)
 

if pantera_negra in playlist_fim_de_semana:
    print('Sim')
else:
    print('Não')